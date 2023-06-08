from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from dao.base import DaoBase, EntityBase
import datetime
import configparser


class GroupId(EntityBase):
    __tablename__ = "group"
    
    group_id = Column(String(10), primary_key = True) #energy onのグループID
    company_name = Column(String(100))


class UserEntity(EntityBase):
    __tablename__ = "user"

    mieruka_user_id = Column(Integer, primary_key = True, autoincrement=True)
    group_id = Column(String(10), unique = False)
    user_name = Column(String(100), unique = False)
    email = Column(String(100), unique = False)
    create_datetime = Column(DateTime, unique = False)
    update_datetime = Column(DateTime, unique = False)
    delete_flg = Column(String(1), unique = False)
    
    def __init__(
        self,
        group_id = None,
        user_name = None,
        email=None,
        create_datetime=None,
        update_datetime=None,
        delete_flg=None,
    ):
        self.group_id = group_id
        self.user_name = user_name
        self.email = email
        self.create_datetime = create_datetime
        self.update_datetime = update_datetime
        self.delete_flg = delete_flg
    
    def __str__(self) -> str:
        f"<mieruka_user_id : {str(self.mieruka_user_id)}, "
        f"group_id: {self.group_id}"
        f"user_name: {self.user_name}"
        f"email: {self.email}"
        f"create_datetime: {self.create_datetime}"
        f"update_datetime: {self.update_datetime}"
        f"delete_flg: {self.delete_flg}>"
    
    

class UserDao(DaoBase):
    def __init__(self, session):
        super().__init__(session)
        
    def insert(self, entity):
        now = self.get_current_datetime()
        entity.create_datetime = now
        entity.update_datetime = now
        entity.delete_flg = "0"
        print(type(entity))
        self.session.add(entity)
        # print(f"=== insert entity. === \n{entity}") idがautoincrementなのでNoneになる。
        
    def update(self, entity):
        entity.update_datetime = self.get_current_datetime()
        # print(f"=== update entity. == \n{entity}")
        
    def delete(self, entity):
        self.session.delete(entity)
        # print(f"=== delete entity. === \n{entity}")
    
    def get_current_datetime(self) -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def select_all(self) -> list[UserEntity]:
        entity_list = []
        for entity in UserEntity.query.order_by(UserEntity.mieruka_user_id):
            entity_list.append(entity)
        return entity_list
    
    def find_by_id(self, mieruka_user_id):
        try:
            return UserEntity.query.filter(UserEntity.mieruka_user_id == mieruka_user_id).with_for_update().one()
        except NoResultFound:
            return None
    
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
        entity_list = []
        q = UserEntity.query
        if group_id != None and group_id != "":
            q = q.filter(UserEntity.group_id.like("%" + group_id + "%"))
        if user_name != None and user_name != "":
            q = q.filter(UserEntity.user_name.like("%" + user_name + "%"))
        if email != None and email != "":
            q = q.filter(UserEntity.email.like("%" + email + "%"))
        if create_datetime_from != None and create_datetime_from != "":
            q = q.filter(
                UserEntity.create_datetime >= create_datetime_from + " 00:00:00"
            )
        if create_datetime_to != None and create_datetime_to != "":
            q = q.filter(UserEntity.create_datetime <= create_datetime_to + " 23:59:59")
        if update_datetime_from != None and update_datetime_from != "":
            q = q.filter(
                UserEntity.update_datetime >= update_datetime_from + " 00:00:00"
            )
        if update_datetime_to != None and update_datetime_to != "":
            q = q.filter(UserEntity.update_datetime <= update_datetime_to + " 23:59:59")
        if delete_flg != None and delete_flg != "":
            q = q.filter(UserEntity.delete_flg == delete_flg)

        for entity in q.order_by(UserEntity.mieruka_user_id):
            entity_list.append(entity)
        return entity_list




#拠点に関するテーブル
class UseBaseEntity(EntityBase):
    __tablename__ = "user_base"
    
    base_id = Column(String(15),primary_key = True)
    group_id = Column(String(10), unique = False)
    address = Column(String(100), unique = False)
    customer_num = Column(String(30), unique = False) #顧客番号
    identification_num = Column(String(30)) #供給地点特定番号
    elec_supply_flg = Column(String(1), unique = False)
    gateway_id = Column(String(30), unique = False)
    create_datetime = Column(DateTime, unique = False)
    update_datetime = Column(DateTime, unique = False)
    delete_flg = Column(String(1), unique = False)
    
    def __init__(
        self,
        service_id=None,
        base_id = None,
        group_id=None,
        adress=None,
        customer_num =None,
        identification_num =None,
        elec_supply_flg =None,
        gateway_id =None,
        create_datetime=None,
        update_datetime=None,
        delete_flg=None,
    ):
        self.base_id =base_id
        self.group_id = group_id
        self.adress = adress
        self.customer_num = customer_num
        self.identification_num = identification_num
        self.elec_supply_flg = elec_supply_flg
        self.gateway_id = gateway_id
        self.create_datetime = create_datetime
        self.update_datetime = update_datetime
        self.delete_flg = delete_flg
    
    def __str__(self) -> str:
        f"base_id: {self.base_id}"
        f"group_id: {self.group_id}"
        f"adress: {self.adress}"
        f"customer_num: {self.customer_num}"
        f"identification_num: {self.identification_num}"
        f"elec_supply_flg: {self.elec_supply_flg}"
        f"gateway_id: {self.gateway_id}"
        f"create_datetime: {self.create_datetime}"
        f"update_datetime: {self.update_datetime}"
        f"delete_flg: {self.delete_flg}>"
        
        
        
