from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from . import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request, abort
from datetime import datetime
import hashlib
import bleach
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from collections import OrderedDict
# from markdown import markdown


#https://gist.github.com/techniq/5174410
class BaseMixin(object):
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    _repr_hide = ['created_at', 'updated_at']

    @classmethod
    def query(cls):
        return db.session.query(cls)

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_by(cls, **kw):
        return cls.query.filter_by(**kw).first()

    @classmethod
    def get_or_404(cls, id):
        rv = cls.get(id)
        if rv is None:
            abort(404)
        return rv

    @classmethod
    def get_or_create(cls, **kw):
        r = cls.get_by(**kw)
        if not r:
            r = cls(**kw)
            db.session.add(r)

        return r

    @classmethod
    def create(cls, **kw):
        r = cls(**kw)
        db.session.add(r)
        return r

    def save(self):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)

    def filter_string(self):
        return self.__str__()

    @property
    def parents(self):
        parents = []
        if hasattr(self, "parent"):
            if hasattr(self.parent, "parent"):
                parents.extend(self.parent.parents)

            parents.append(self.parent)

        return parents

    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result

    def __repr__(self):
        values = ', '.join("%s=%r" % (n, getattr(self, n)) for n in self.__table__.c.keys() if n not in self._repr_hide)
        return "%s(%s)" % (self.__class__.__name__, values)

class UserMixin(UserMixin, BaseMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    phone_number = db.Column(db.Integer, unique=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar_hash = db.Column(db.String(32))
    address1 = db.Column(db.String(128))
    address2 = db.Column(db.String(128))
    location = db.Column(db.String(64))

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def generate_auth_token(self, epiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=epiration)
        return s.dumps({'id' : self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return user.query.get(data['id'])



    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable  attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def gravatar(self, size=100, default = 'identicon', rating='g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        hash = self.avatar_hash or\
         hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size,
            default=default, rating=rating)

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return self.id
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __eq__(self, other):
        '''
        Checks the equality of two `UserMixin` objects using `get_id`.
        '''
        if isinstance(other, UserMixin):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        '''
        Checks the inequality of two `UserMixin` objects using `get_id`.
        '''
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal

Teacher_Subject = db.Table('Teacher_Subject',
                           db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id')),
                           db.Column('subject_id', db.Integer, db.ForeignKey('subjects.id')),
                           db.PrimaryKeyConstraint('teacher_id', 'subject_id') )

# School_Credit = db.Table('School_Credit',
#                            db.Column('school_id', db.Integer, db.ForeignKey('schools.id')),
#                            db.Column('credit_id', db.Integer, db.ForeignKey('credits.id')),
#                            db.PrimaryKeyConstraint('school_id', 'credit_id') )

class User(db.Model, UserMixin):
    __tablename__="users"
    is_admin = db.Column(db.Boolean, default=False)

    def is_administrator(self):
        return self.is_admin


class Teacher(User):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
    fullname = db.Column(db.String(64))
    sex = db.Column(db.Boolean)
    job_history = db.Column(db.Text)
    educational_history = db.Column(db.Text)
    certifications = db.Column(db.Text)
    references = db.Column(db.Text)
    searching = db.Column(db.Boolean)
    subjects = db.relationship('Subject', secondary=Teacher_Subject, backref="teachers")

class School(User):
    __tablename__ = 'schools'
    id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
    profile_form = db.Column(db.Text)
    # credits = db.relationship('Credit', secondary=School_Credit, backref=schools)
    credits = db.Column(db.Integer)
    website = db.Column(db.String(128))
    ads = db.relationship('Ad', backref='school', lazy = 'dynamic')


class Subject(db.Model, BaseMixin):
    __tablename__='subjects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    ads = db.relationship('Ad', backref='subject', lazy = 'dynamic')

class Ad(db.Model, BaseMixin):
    __tablename__="ads"
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))
    school_id = db.Column(db.Integer, db.ForeignKey("schools.id"))
    approved = db.Column(db.Boolean)
    post_publish = db.Column(db.DateTime, default=datetime.utcnow)
    experience = db.Column(db.Integer)
    description = db.Column(db.Text)
    salary_expectation = db.Column(db.Float)

    def approve(self):
        if not self.approved:
            self.approved=True
            self.post_publish=datetime.utcnow()
            db.session.add(self)


# class Credit(db.Model, BaseMixin):
#     __tablename__='credits'
#     id = db.Column(db.Integer, primary_key=True)
#     value = db.Column(db.Integer)
#     name = db.Column(db.String(64))

class AnonymousUser(AnonymousUserMixin):

    def is_administrator(self):
        return False

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
login_manager.anonymous_user = AnonymousUser
