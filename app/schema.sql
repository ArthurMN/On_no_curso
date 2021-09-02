DROP TABLE IF EXISTS cursos;

CREATE TABLE "cursos" (
	"id"	INTEGER,
	"nome_curso"	TEXT NOT NULL,
	"nome_facilitador"	TEXT NOT NULL,
	"preco"	REAL NOT NULL,
	"data"	NUMERIC NOT NULL,
	"link"	TEXT NOT NULL,
	"validacao"	TEXT NOT NULL,
	PRIMARY KEY("id")
);