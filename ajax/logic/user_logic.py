from dao.base import DBSessionFactory
from dao.user_dao import UserEntity, UseBaseEntity, UserDao
# from util.logger_factory import LoggerFactory

# logger = LoggerFactory.getLogger(__name__)



class UserEntityLogic:
    def insert(self, group_id, user_name, email):
        session = DBSessionFactory.get_session()
        dao = UserDao(session)
        
        try:
            entity = UserEntity(group_id ,user_name, email)
            dao.insert(entity)
            session.commit()
            return entity.user_name

        except Exception as ex:
            # logger.error("Unexpected error occurred.", exc_info=ex)
            session.rollback()
            raise ex
            
        finally:
            session.close()
            
    def update(self, mieruka_user_id, email):
        session = DBSessionFactory.get_session()
        dao = UserDao(session)
        
        try:
            entity = dao.find_by_id(mieruka_user_id)
            entity.email = email
            dao.update(entity)
            session.commit()
            
        except Exception as ex:
            # logger.error("Unexpected error occurred.", exc_info=ex)
            session.rollback()
            raise ex
        
        finally:
            session.close()
            
    def delete(self, mieruka_user_id):
        session = DBSessionFactory.get_session()
        dao = UserDao(session)
        
        try:
            entity = dao.find_by_id(mieruka_user_id)
            dao.delete(entity)
            session.commit()
            
        except Exception as ex:
            # logger.error("Unexpected error occureed.", exc_info = ex)
            raise ex
        
        finally:
            session.close()
            
    def select_all(self) -> list[UserEntity]:
        session = DBSessionFactory.get_session()
        dao = UserDao(session)
        
        try:
            return dao.select_all()
        
        except Exception as ex:
            # logger.error("Unexpected error occureed.", exc_info = ex)
            raise ex
        
        finally:
            session.close()    
        
    def find_by_email(self, email):
        session = DBSessionFactory.get_session()
        dao = UserDao(session)
        try:
            return dao.find_by_email(email)

        except Exception as ex:
            # logger.error("Unexpected error occurred.", exc_info=ex)
            raise ex

        finally:
            session.close()
        
    def search(
            self,
            mieruka_user_id,
            group_id,
            user_name,
            email,
            create_datetime_from,
            create_datetime_to,
            update_datetime_from,
            update_datetime_to,
            delete_flg
    ):
        session = DBSessionFactory.get_session()
        dao = UserDao(session)

        try:
            return dao.search(
                mieruka_user_id,
                group_id,
                user_name,
                email,
                create_datetime_from,
                create_datetime_to,
                update_datetime_from,
                update_datetime_to,
                delete_flg
            )

        except Exception as ex:
            # logger.error("Unexpected error occurred.", exc_info=ex)
            session.rollback()
            raise ex

        finally:
            session.close()


if __name__ == "__main__":
    
    create = DBSessionFactory()
    create.create_datebase()
    
    ul = UserEntityLogic()

    # username = ul.insert(134, "yoshida", "yoshida@mail")
    # print(f"username: {username}")

    # update = ul.update(4, email="update@")

    data = ul.select_all()

    for r in data:
        recode = f" id:{r.mieruka_user_id}, group_id: {r.group_id},\
                user_name:{r.user_name}, email: {r.email}"
            
        print(recode)    

    # ul.delete(2)