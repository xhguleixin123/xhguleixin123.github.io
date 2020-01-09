import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt='%Y-%m-%d  %H:%M:%S %a',
                    )
logging.debug('msg1')
logging.info('msg2')
logging.warning('%s is %d years old','Tom',10)
logging.error('msg4')
logging.critical('msg5')