import __init__
from models.database import engine
from sqlmodel import Session, select
from datetime import date
from models.model import Subscription


class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine


    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            #session.refresh(subscription)
            return subscription
        
    def list_all(self):
        with Session(self.engine) as sesion:
            statement = select(Subscription)
            results = sesion.exec(statement).all()

            return results

ss = SubscriptionService(engine)

#subscription = Subscription(empresa='teste', site='teste.com.br', data_assinatura=date.today(), valor=37.90)
#ss.create(subscription)

print(ss.list_all())


