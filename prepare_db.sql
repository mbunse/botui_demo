CREATE USER chatbotts IDENTIFIED BY chooseapasswordandinserthere;
GRANT CREATE TABLE, DELETE ANY TABLE, INSERT ANY TABLE, SELECT ANY TABLE, CREATE SESSION, CREATE SEQUENCE to chatbotts; 
GRANT unlimited tablespace to chatbotts;

--DROP TABLE chatbotts.EVENTS;