import logging

"""for reference use github: https://github.com/CoreyMSchafer/code_snippets/blob/master/Logging-Advanced/log-sample.py"""
class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
        file_handler = logging.FileHandler("Logs/automation.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

"""If you want print log in console use below logger class"""
# class LogGen:
#     @staticmethod
#     def loggen():
#         logger = logging.getLogger(__name__)
#         logger.setLevel(logging.INFO)
#         formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
#         file_handler = logging.FileHandler("Logs/automation.log")
#         file_handler.setFormatter(formatter)
#         stream_handler = logging.StreamHandler()
#         stream_handler.setFormatter(formatter)
#         logger.addHandler(file_handler)
#         logger.addHandler(stream_handler)
#         return logger

