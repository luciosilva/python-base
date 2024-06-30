#!/usr/bin/env python3

#python logs.py &2> /tmp/error.log
import os
import logging
from logging import handlers


# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARING").upper()
#export LOG_LEVEL=error
#export LOG_LEVEL=debug

#logging  #root logger

# nossa instancia
#log = logging.Logger("logs.py", "DEBUG")
#log = logging.Logger("logs.py", 10)
log = logging.Logger("logs.py", log_level)

# level
#ch = logging.StreamHandler() # Console/terminal/stderr
#ch.setLevel(log_level)

#fh = handlers.RotatingFileHandler("meulog.log", maxBytes=10**6)#comum a ser usado
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=300, # 10**6
    backupCount=10
)
fh.setLevel(log_level)

# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)
# destino
#log.addHandler(ch)
log.addHandler(fh)
"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))