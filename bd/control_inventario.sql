PGDMP  4                    |            control_inventario    16.2    16.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16396    control_inventario    DATABASE     �   CREATE DATABASE control_inventario WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
 "   DROP DATABASE control_inventario;
                postgres    false            �            1259    24577 
   inventario    TABLE     �   CREATE TABLE public.inventario (
    id integer NOT NULL,
    nombre character varying(100),
    codigo character varying(20),
    cantidad integer,
    categoria character varying(50),
    descripcion character varying(100)
);
    DROP TABLE public.inventario;
       public         heap    postgres    false            �            1259    24576    inventario_id_seq    SEQUENCE     �   CREATE SEQUENCE public.inventario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.inventario_id_seq;
       public          postgres    false    218            �           0    0    inventario_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.inventario_id_seq OWNED BY public.inventario.id;
          public          postgres    false    217            �            1259    16407    usuarios    TABLE     A  CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nombre character varying(100),
    apellido character varying(100),
    id_usuario character varying(20),
    telefono character varying(20),
    username character varying(50),
    password character varying(100),
    es_administrador boolean DEFAULT false
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false            �            1259    16406    usuarios_id_seq    SEQUENCE     �   CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.usuarios_id_seq;
       public          postgres    false    216            �           0    0    usuarios_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;
          public          postgres    false    215            W           2604    24580    inventario id    DEFAULT     n   ALTER TABLE ONLY public.inventario ALTER COLUMN id SET DEFAULT nextval('public.inventario_id_seq'::regclass);
 <   ALTER TABLE public.inventario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217    218            U           2604    16416    usuarios id    DEFAULT     j   ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);
 :   ALTER TABLE public.usuarios ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            �          0    24577 
   inventario 
   TABLE DATA           Z   COPY public.inventario (id, nombre, codigo, cantidad, categoria, descripcion) FROM stdin;
    public          postgres    false    218   5       �          0    16407    usuarios 
   TABLE DATA           t   COPY public.usuarios (id, nombre, apellido, id_usuario, telefono, username, password, es_administrador) FROM stdin;
    public          postgres    false    216   �       �           0    0    inventario_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.inventario_id_seq', 20, true);
          public          postgres    false    217            �           0    0    usuarios_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.usuarios_id_seq', 1, true);
          public          postgres    false    215            ]           2606    24584     inventario inventario_codigo_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.inventario
    ADD CONSTRAINT inventario_codigo_key UNIQUE (codigo);
 J   ALTER TABLE ONLY public.inventario DROP CONSTRAINT inventario_codigo_key;
       public            postgres    false    218            _           2606    24582    inventario inventario_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.inventario
    ADD CONSTRAINT inventario_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.inventario DROP CONSTRAINT inventario_pkey;
       public            postgres    false    218            Y           2606    16413    usuarios usuarios_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_pkey;
       public            postgres    false    216            [           2606    16415    usuarios usuarios_username_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_username_key UNIQUE (username);
 H   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_username_key;
       public            postgres    false    216            �   j  x�m�Kn�0���)8A'��2���
��~	#�Q;iwb�#p�:F��z>�?3fX�Z�3"����FT������h� u�ܫ�Y->�~�$
Z�w�j��\d7f��K^�9� ����a��6�:iE��?�RT���/[��cDJR�Ӊ�Ě3ϒk����S%t�%��c���+�i����_)�D%j�7G6����0#]i �Yd��}4�����Z�-1zX�yXPv e���T`Mm	��5@�T��n���|��H�k��ۭ�x��T~�ʩV%�Ȯ�u���L�����F��i��Zp�`Z���N�#�Yy(%�ئ��	6b�n��dy�f>�oI���Y�
�O&�m���}��z��L�#      �   )   x�3�tL����,.)JL�/B�r�r&���d	W� ���     