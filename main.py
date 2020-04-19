# from app.data.db_session import global_init, create_session
# from app.data.users import User
# from app.data.jobs import Jobs

addr = input()
global_init(addr)
session = create_session()

q = session.query(User).filter(
    User.address == 'module_1',
    User.speciality.notlike('%ingeneer%'),
    User.position.notlike('%ingeneer%')
)

for user in q.all():
    print(user.id)
