#!/usr/bin/env python3
import random
from faker import Faker

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Audition, Role

if __name__ == '__main__':
    engine = create_engine('sqlite:///theaters.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.query(Audition).delete()
    session.query(Role).delete()
        
    fake = Faker()
    
    locations = ['Nairobi', 'Mombasa', 'Eldoret', 'Nakuru', 'Kisumu']
    
    hired_options = [False, True]
    
    roles = []
    for i in range(10):
        role = Role(character_name=fake.name())
        
        session.add(role)
        session.commit()
        
        roles.append(role)
        
    auditions = []    
    for role in roles:
        for i in range(random.randint(0,4)):
            audition = Audition(actor=fake.name(), location=random.choice(locations), phone=random.randint(0,100), hired=random.choice(hired_options), role_id=role.id)
            
            auditions.append(audition)
            
    session.bulk_save_objects(auditions)
    session.commit()
    
    new_role = Role(character_name=fake.name())
    session.add(new_role)
    session.commit()
    
    new_audition = Audition(actor=fake.name(), location=random.choice(locations), phone=random.randint(0,100), hired=False, role_id=new_role.id)
    session.add(new_audition)
    session.commit()
    session.close()