/****** Script for SelectTopNRows command from SSMS  ******/
SET IDENTITY_INSERT [dbo].[planificaciones_estrategiasens] ON
INSERT INTO [dbo].[planificaciones_estrategiasens] (id, [key], estrategia)
VALUES (1,'ABP',  'Aprendizaje basado en problemas' ),
       (2,'APP',  'Aprendizaje por proyectos' ),
	   (3,'EC',  'Estudio de casos' ),
	   (4,'S',  'Simulación' ),
	   (5,'AI',  'Aprendizaje Invertido' ),
	   (6,'TE',  'Trabajo en Equipos' ),
	   (7,'AC',  'Aprendizaje Colaborativo' ),
	   (8,'E',  'Ensayo' ),
	   (9,'EA',  'Elaboración de Artículos' ),
	   (10,'MRC',  'Mapas mentales y redes conceptuales' ),
	   (11,'P',  'Panel' ),
	   (12,'TR',  'Taller reflexivo' ),
	   (13,'SEM',  'Seminarios' ),
	   (14,'ITP',  'Investigación de tópicos y problemas específicos' ),
	   (15,'IL',  'Informe de Lectura' ),
	   (16,'D',  'Debates' ),
	   (17,'PF',  'Pasantías formativas' ),
	   (18,'JR',  'Juego de roles' ),
	   (19,'O',  'Otros' );
SET IDENTITY_INSERT [dbo].[planificaciones_estrategiasens] OFF 