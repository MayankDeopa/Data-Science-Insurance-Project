from insurance.logger import logging
from insurance.exception import InsuranceException

import sys, os
 
def test_logger_and_expetion():



   try:


      logging.info("Starting the test_logger_and_exception")
      result = 3/0
      print(result)
      logging.info("Stoping the test_logger_and_exception")
   except Exception as e:

      logging.debug(str(e))
      raise InsuranceException(e, sys)

if __name__=="__main__":
   try:
      test_logger_and_expetion()
   except Exception as e:
      print(e)   