from api.infra.db.factory import postgres_factory
import logging

LOGGER = logging.getLogger(__name__)

def test_select_from_postgres():
  driver = postgres_factory()
  data = driver.select_all()
  LOGGER.info("Quantidade de dados na tabela: %s", len(data))
  
  assert type(data) is list 
  