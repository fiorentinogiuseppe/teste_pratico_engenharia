SELECT *
FROM processos
INNER JOIN andamentos ON processos.id=andamentos.processos_id;