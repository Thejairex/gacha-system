from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class DB:
    def __init__(self) -> None:
        """
        Engine and Session initialization
        
        """
        self.engine = create_engine("sqlite:///gacha.db")
        self.session = sessionmaker(bind=self.engine)
        self.session = self.session()

    def create_tables(self):
        """
        Creates the tables in the database if they don't exist.
        
        returns: None
        """
        Base.metadata.create_all(self.engine)

    def add(self, model):
        """
        Adds a model object to the database and commits the changes. \n
        If the model is a list, it adds all the objects in the list to the database and commits the changes.
        args:
            model: The model object to be added to the database (Base or a list of Base).
            
        returns: None
        """
        if isinstance(model, list): self.session.add_all(model)
        else: self.session.add(model)
        self.commit()
        
    def __order_by(self, query, model, order_by, order):
        """
        Private method for ordering the query
        
        args:
            query: The query to be ordered.
            order_by: The column name to be used for ordering.
            order: The order to be used for ordering (optional, default is "asc").
            
        returns: The ordered query.
        """
        if order == "asc":
            return query.order_by(getattr(model, order_by))

        elif order == "desc":
            return query.order_by(getattr(model, order_by).desc())

    def get_all(self, model, order_by: str = None, order="asc"):
        """
        Gets all the model objects from the database.
        
        args:
            model: The model object to be added to the database (Base).
            order_by: The column name to be used for ordering (optional).
            order: The order to be used for ordering (optional, default is "asc").
            
        returns: A list of model objects.
        """
        query = self.session.query(model)
        
        if order_by:
            query = self.__order_by(query, model, order_by, order)
            
        return query.all()

    def get_where(self, model, column, value, order_by: str = None, order="desc"):
        """
        Gets all the model objects from the database that match the given column and value.
        
        args:
            model: The model object to be added to the database (Base).
            column: The column name to be used for filtering.
            value: The value to be used for filtering.
            order_by: The column name to be used for ordering (optional).
            order: The order to be used for ordering (optional, default is "desc").
        
        returns: A list of model objects that match the given column and value.
        """
        query = self.session.query(model).filter(getattr(model, column) == value)
        
        if order_by:
            query = self.__order_by(query, model, order_by, order)
        
        return query.all()

    def get_record(self, model, column, value):
        return self.session.query(model).filter(getattr(model, column) == value).first()
    
    def get_last_record(self, model, column_id="id"):
        """
        Gets the last model object from the database.
        
        args:
            model: The model object to be added to the database (Base).
            column_id: The column name to be used for ordering by id (default is "id").
            
        returns: The last model object in the database.
        """
        return self.session.query(model).order_by(getattr(model, column_id).desc()).first()

    def get_where_record(self, model, column, value, order_by=None, order="desc"):
        """
        Gets the first model object from the database that matches the given column and value.
        
        args:
            model: The model object to be added to the database (Base).
            column: The column name to be used for filtering.
            value: The value to be used for filtering.
            order_by: The column name to be used for ordering (optional).
            order: The order to be used for ordering (optional, default is "desc").
        
        returns: The first model object that matches the given column and value.
        """
        
        query = self.session.query(model).filter(getattr(model, column) == value)
        
        if order_by:
            query = self.__order_by(query, order_by, order)
        
        return query.first()

    def delete_record(self, model, column, value):
        self.session.query(model).filter(
            getattr(model, column) == value).delete()
        self.commit()

    def update(self, model, column_id = "id"):
        pass
    
    def rollback(self):
        self.session.rollback()
        
    def commit(self):
        self.session.commit()

    def close(self):
        self.session.close()