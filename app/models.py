from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Writer class Model
class User(db.Model):
    __tablename__= 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    username = db.Column(db.String(255), unique=True,nullable=False)
    email = db.Column(db.String(255), unique=True,nullable=False)
    about = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255),nullable=False)
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)
    
    def __repr__(self):
        return f"User {self.username}"

# Subscribers class Model
class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),unique=False)
    email = db.Column(db.String(255),unique=True)
    
    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.name}'
   
# Role class Model
class Role(db.Model):
    __tablename__= 'roles'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy='dynamic')
    
    def save_role(self):
        db.session.add(self)
        db.session.commit()
    
# Blog class Model
class Blog(db.Model):
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(255),index=True, nullable=True)
    blog = db.Column(db.String(255),nullable=False)
    blog_time = db.Column(db.DateTime, default=datetime.utcnow)

    def save_blog(self):
        db.session.add(self)
        db.session.commit()
        
    def get_blog(self,id):
        blog = Blog.query.filter_by(id=id).first()
        return blog
        
    @classmethod
    def del_blog(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'Blog {self.title}'

# Comment class Model
# Vote class Model
