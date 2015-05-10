import datetime

from ziggurat_provision import db, Server

db.create_all()

a = Server('64-14-00-00-01', 'vm01', 'IN_USE', 'KVM', datetime.datetime.utcnow(), datetime.datetime.utcnow())

print a

db.session.add(a)

db.session.commit()

print Server.query.all()
#
# CREATE TABLE server (
# mac varchar(17) primary key,
# hostname varchar(255) not null unique,
# state varchar(64) not null,
# profile varchar(64) not null,
# created integer not null,
# updated integer not null
# );
#
# INSERT into server values('64-14-00-00-01', 'vm01', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-02', 'vm02', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-03', 'vm03', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-04', 'vm04', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-05', 'vm05', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-06', 'vm06', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-07', 'vm07', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-08', 'vm08', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-09', 'vm09', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-0a', 'vm10', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-0b', 'vm11', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-0c', 'vm12', 'WARLOCK', 'KVM', 1428288917, 1428288917);
# INSERT into server values('64-14-00-00-0d', 'vm13', 'WARLOCK', 'KVM', 1428288917, 1428288917);
