CREATE database cadastros;

\c cadastros;

CREATE TABLE "tabela" (
    id SERIAL PRIMARY KEY,
    email VARCHAR(200) UNIQUE NOT NULL
);

INSERT INTO tabela VALUES (DEFAULT,'teste@gmail.com');
INSERT INTO tabela VALUES (DEFAULT,'joao@gmail.com');