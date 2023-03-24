CREATE DATABASE gis WITH TEMPLATE = template0 ENCODING = 'UTF8';

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;;

SET search_path = public, pg_catalog;
SET default_tablespace = '';
SET default_with_oids = false;

CREATE TABLE geolocation (
    id BIGINT NOT NULL,
    x FLOAT NOT NULL,
    y FLOAT NOT NULL,
    importance FLOAT NOT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS geolocation_importance
  ON geolocation 
  USING btree (importance);

CREATE TABLE topology(
    loc1_id BIGINT NOT NULL,
    loc2_id BIGINT NOT NULL,
    distance FLOAT NOT NULL,
    FOREIGN KEY (loc1_id) REFERENCES geolocation (id) ON DELETE CASCADE,
    FOREIGN KEY (loc2_id) REFERENCES geolocation (id) ON DELETE CASCADE,
    PRIMARY KEY (loc1_id, loc2_id)
);
