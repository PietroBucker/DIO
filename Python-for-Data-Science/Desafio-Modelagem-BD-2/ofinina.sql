-- Criando tabela
create database oficinia;
use ecommerce;

CREATE TABLE IF NOT EXISTS Cliente (
  idCliente INT NOT NULL AUTO_INCREMENT,
  Pnome VARCHAR(15) NOT NULL,
  NMeioInicial VARCHAR(3) NULL,
  Sobrenome VARCHAR(20) NULL,
  CPF CHAR(11) NOT NULL,
  Endereço VARCHAR(45) NULL,
  DataDeNascimento DATE NOT NULL,
  PRIMARY KEY (idCliente),
  UNIQUE INDEX Identificação_UNIQUE (CPF ASC) VISIBLE);


DROP TABLE IF EXISTS oficina.Pedido ;

CREATE TABLE IF NOT EXISTS oficina.Pedido (
  idPedido INT NOT NULL,
  Status ENUM('Processando', 'Enviado', 'Entregue') NULL DEFAULT 'Processando',
  Descrição VARCHAR(45) NULL,
  DataPedido DATE NULL,
  Cliente_idCliente INT NOT NULL,
  PRIMARY KEY (idPedido, Cliente_idCliente),
  INDEX fk_Pedido_Cliente_idx (Cliente_idCliente ASC) VISIBLE,
  CONSTRAINT fk_Pedido_Cliente
    FOREIGN KEY (Cliente_idCliente)
    REFERENCES oficina.Cliente (idCliente)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


DROP TABLE IF EXISTS oficina.Servico ;

CREATE TABLE IF NOT EXISTS oficina.Servico (
  idServico INT NOT NULL,
  Categoria VARCHAR(45) NULL,
  Descrição VARCHAR(45) NULL,
  Valor VARCHAR(45) NULL,
  PRIMARY KEY (idServico))
ENGINE = InnoDB;


DROP TABLE IF EXISTS oficina.mecanico ;

CREATE TABLE IF NOT EXISTS oficina.mecanico (
  idMecanico INT NOT NULL,
  RazaoSocial VARCHAR(45) NULL,
  CNPJ VARCHAR(45) NULL,
  PRIMARY KEY (idMecanico))
ENGINE = InnoDB;


DROP TABLE IF EXISTS oficina.Disponibiliza ;

CREATE TABLE IF NOT EXISTS oficina.Disponibiliza (
  mecanico_idMecanico INT NOT NULL,
  servico_idServico INT NOT NULL,
  PRIMARY KEY (mecanico_idMecanico, servico_idServico),
  INDEX fk_mecanico_has_Servico_servico1_idx (servico_idServico ASC) VISIBLE,
  INDEX fk_mecanico_has_Servico_mecanico1_idx (mecanico_idMecanico ASC) VISIBLE,
  CONSTRAINT fk_mecanico_has_Servico_mecanico1
    FOREIGN KEY (mecanico_idMecanico)
    REFERENCES oficina.mecanico (idMecaninco)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Fornecedor_has_Servico_servico1
    FOREIGN KEY (servico_idServico)
    REFERENCES oficina.servico (idServico)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS RelaçaServicoPedido (
  Servico_idServico INT NOT NULL,
  Pedido_idPedido INT NOT NULL,
  Quantidade INT NOT NULL DEFAULT 0,
  Status ENUM('Disponível', 'Indisponivel') NULL DEFAULT 'disponível',
  PRIMARY KEY (Servico_idServico, Pedido_idPedido),
  INDEX fk_Servico_has_Pedido_Pedido1_idx (Pedido_idPedido ASC) VISIBLE,
  INDEX fk_Servico_has_Pedido_Servico1_idx (Servico_idServico ASC) VISIBLE,
  CONSTRAINT fk_Servico_has_Pedido_Servico1
    FOREIGN KEY (Servico_idServico)
    REFERENCES oficina.Servico (idServico)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Servico_has_Pedido_Pedido1
    FOREIGN KEY (Pedido_idPedido)
    REFERENCES oficina.Pedido (idPedido)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- Table ecommerce.Entrega
-- DROP TABLE IF EXISTS ecommerce.Entrega ;

CREATE TABLE IF NOT EXISTS oficina.Entrega (
  idEntrega INT NOT NULL,
  CodigoRastreio VARCHAR(45) NULL,
  DataEnvio VARCHAR(45) NULL,
  DataEntrega VARCHAR(45) NULL,
  Status VARCHAR(45) NULL,
  Pedido_idPedido INT NOT NULL,
  PRIMARY KEY (idEntrega, Pedido_idPedido),
  INDEX fk_Entrega_Pedido1_idx (Pedido_idPedido ASC) VISIBLE,
  CONSTRAINT fk_Entrega_Pedido1
    FOREIGN KEY (Pedido_idPedido)
    REFERENCES oficina.Pedido (idPedido)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;











