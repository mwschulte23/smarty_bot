from sqlalchemy import create_engine

class DatabaseAdapter:
    def __init__(self, time_num, time_dim):
        self.uri = 'postgresql+psycopg2://mike:mike@localhost:5432/jaffle_shop'
        self.time_num = time_num
        self.time_dim = time_dim

    def query_db(self):
        q = f"select count(distinct customer_id) customers \
        from dbt_alice.customers where first_order >= current_date - interval '{self.time_num} {self.time_dim}' ".format()

        with create_engine(self.uri).connect() as conn:
            result = conn.execute(q)

            out = [r['customers'] for r in result]

        return str(out[0])



