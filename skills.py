import pandas as pd
from crud_operations import CrudOperations
from config import Config


class Skills:
    """
    Skills class
    """

    def get_top_skills(self, no_of_skills: int) -> pd.DataFrame:
        """
        THis method gets all top skills
        :param no_of_skills:
        :return pd.DataFrame
        """

        query = f"""select id count(id), name from skills group by id,name
                  limit {no_of_skills}"""
        return CrudOperations.read_data(query, Config.connection_url)
