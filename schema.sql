drop table if exists facilitador;

create table facilitador(
	id integer primary key autoincrement,
	nome_facilitador text not null,
	nome_curso text not null,
	preco float not null,
	data datetime not null,
	link text not null
);