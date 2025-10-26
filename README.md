# 📰 Blog em Django

![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

## 📖 Sobre o Projeto

Este é um **sistema de blog desenvolvido em Python e Django** como parte de um projeto acadêmico.  
O objetivo é criar uma aplicação funcional que permita **gerenciar posts, tags e comentários**, com autenticação de usuários e interface administrativa moderna via **Django Jazzmin**.

---

## 🧩 Funcionalidades

- 🧑‍💻 **Autenticação de Usuários** (com Django padrão)  
- 📝 **CRUD completo de Posts** (criar, editar, excluir e listar)
- 🏷️ **Sistema de Tags** com relação *ManyToMany*
- 💬 **Sistema de Comentários** por post
- ⏰ **Controle automático de datas** (criação e atualização)
- 🧭 **Painel administrativo estilizado com Jazzmin**
- 🔐 **Integração com JWT (SimpleJWT)** para autenticação de API
- 🌐 **CORS liberado** para uso com frontends externos
- 📘 **Documentação interativa da API** (Swagger / ReDoc via `drf-yasg`)

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|--------------|
| Backend | Python, Django, Django REST Framework |
| Autenticação | SimpleJWT |
| Banco de Dados | PostgreSQL |
| Documentação da API | drf-yasg, Django REST Swagger |
| Frontend (Admin) | Django Jazzmin |
| Outras libs | Requests, PyYAML, CORS Headers |
