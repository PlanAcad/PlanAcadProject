
SET IDENTITY_INSERT [dbo].[planificaciones_categoria] ON
INSERT INTO [dbo].[planificaciones_categoria] (id, categoria)
VALUES (2, 'Titular' ),
       (4, 'JTP' ),
	   (5, 'Adjunto' ),
	   (6, 'Asociado' ),
	   (7, 'ATP de Primera' ),
	   (8, 'ATP de Segunda' );
SET IDENTITY_INSERT [dbo].[planificaciones_categoria] OFF 