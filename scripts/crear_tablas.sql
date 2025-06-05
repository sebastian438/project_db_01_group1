CREATE TABLE Alumno (
    id_alumno SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(50)
);

CREATE TABLE Profesor (
    id_profesor SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    rol VARCHAR(30)
);

CREATE TABLE Vertical (
    id_vertical SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE Proyecto (
    id_proyecto SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
	id_vertical INT,
    FOREIGN KEY (id_vertical) REFERENCES Vertical(id_vertical)
);

CREATE TABLE Evaluacion (
    id_evaluacion SERIAL PRIMARY KEY,
    resultado VARCHAR(20),
    id_alumno INT,
    id_proyecto INT,
    FOREIGN KEY (id_alumno) REFERENCES Alumno(id_alumno),
    FOREIGN KEY (id_proyecto) REFERENCES Proyecto(id_proyecto)
);

CREATE TABLE Curso (
    id_curso SERIAL PRIMARY KEY,
    campus VARCHAR(100),
    promocion VARCHAR(100),
    modalidad VARCHAR(100),
    id_vertical INT,
    id_profesor_principal INT,
    id_profesor_apoyo INT,
    FOREIGN KEY (id_vertical) REFERENCES Vertical(id_vertical),
    FOREIGN KEY (id_profesor_principal) REFERENCES Profesor(id_profesor),
    FOREIGN KEY (id_profesor_apoyo) REFERENCES Profesor(id_profesor)
);

CREATE TABLE Fecha_comienzo (
    id_comienzo SERIAL PRIMARY KEY,
    fecha_comienzo DATE,
    id_alumno INT,
    id_curso INT,
    FOREIGN KEY (id_alumno) REFERENCES Alumno(id_alumno),
    FOREIGN KEY (id_curso) REFERENCES Curso(id_curso)
);



