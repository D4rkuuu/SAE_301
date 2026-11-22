DROP TABLE IF EXISTS Fact_Indicateur;
DROP TABLE IF EXISTS Dim_Modele;
DROP TABLE IF EXISTS Dim_Horizon;
DROP TABLE IF EXISTS Dim_Culture;
DROP TABLE IF EXISTS Dim_Commune;


CREATE TABLE Dim_Commune (
    code_insee VARCHAR(5) PRIMARY KEY,
    nom VARCHAR(100),
    latitude DECIMAL(8, 5),
    longitude DECIMAL(8, 5),
    altitude_m INT,
    zone_climatique VARCHAR(50)
);

CREATE TABLE Dim_Culture (
    id_culture INT PRIMARY KEY,
    nom VARCHAR(50),
    t_base_c DECIMAL(4, 1),
    gdd_maturite_cj INT,
    seuil_gel_c DECIMAL(4, 1),
    besoin_eau_mm INT,
    t_opt_min_c DECIMAL(4, 1),
    t_opt_max_c DECIMAL(4, 1),
    seuil_stress_c DECIMAL(4, 1)
);

CREATE TABLE Dim_Horizon (
    id_horizon INT AUTO_INCREMENT PRIMARY KEY,
    label VARCHAR(20),
    annee_debut INT,
    annee_fin INT
);

CREATE TABLE Dim_Modele(
    id_modele INT PRIMARY KEY, 
    nom_modele VARCHAR(50),
    organisme VARCHAR(100)
);

CREATE TABLE Fact_Indicateur (
    id_fait INT AUTO_INCREMENT PRIMARY KEY,
    code_insee VARCHAR(5) NOT NULL,
    id_culture INT NOT NULL,
    id_horizon INT NOT NULL,
    id_modele INT NOT NULL, 
    id_session VARCHAR(64),
    gdd_cumul_moyen DECIMAL(7, 1),
    nb_jours_gel DECIMAL(4, 1),
    nb_jours_stress_th DECIMAL(4, 1),
    bilan_hydrique_mm DECIMAL(6, 1),
    verdict VARCHAR(20),

       CONSTRAINT uq_fact_session UNIQUE (id_session, code_insee, id_culture, id_horizon, id_modele),
    CONSTRAINT fk_fact_commune FOREIGN KEY (code_insee) REFERENCES Dim_Commune(code_insee),
    CONSTRAINT fk_fact_culture FOREIGN KEY (id_culture) REFERENCES Dim_Culture(id_culture),
    CONSTRAINT fk_fact_horizon FOREIGN KEY (id_horizon) REFERENCES Dim_Horizon(id_horizon),
    CONSTRAINT fk_fact_modele FOREIGN KEY (id_modele) REFERENCES Dim_Modele(id_modele)
);
