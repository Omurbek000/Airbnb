# 🏨 Airbnb Clone API

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-green)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-red)](https://www.django-rest-framework.org/)

Полнофункциональный бэкенд для платформы бронирования жилья, вдохновлённой Airbnb. Проект предоставляет мощный REST API для управления отелями, номерами, бронированиями и пользователями.

![Airbnb Clone API](https://via.placeholder.com/800x400.png?text=Airbnb+Clone+API)

## 📋 О проекте

Этот проект является клоном популярного сервиса Airbnb, разработанным на Django и Django REST Framework (DRF). Он реализует базовый функционал современного сервиса бронирования, включая регистрацию пользователей, управление отелями и номерами, а также систему бронирования.

Проект демонстрирует глубокое понимание бэкенд-разработки, работы с базами данных, создания RESTful API и реализации сложной бизнес-логики.

## ✨ Ключевые возможности

- **👤 Пользователи и аутентификация**
  - Кастомная модель пользователя с ролями (Администратор, Пользователь, Гость).
  - Регистрация и аутентификация с использованием JWT-токенов.
  - Вход через социальные сети (Google, GitHub) с помощью `django-allauth`.

- **🏨 Управление контентом**
  - **Страны и города**: Иерархическая структура местоположений.
  - **Отели**: Полный CRUD для отелей с возможностью фильтрации, поиска и сортировки.
  - **Удобства (Amenities)**: Управление списком удобств для отелей/номеров.
  - **Номера (Rooms)**: Управление номерами, их типом, ценой и доступностью.

- **📅 Бронирования**
  - Создание, просмотр и отмена бронирований.
  - Проверка доступности номеров на выбранные даты.

- **⭐ Отзывы и рейтинги**
  - Возможность оставлять отзывы на отели и номера.
  - Система рейтинга для оценки качества.

- **💳 Платежи**
  - Интеграция с платёжной системой Stripe для обработки оплат.

- **📚 Документация API**
  - Автоматически генерируемая документация Swagger UI (доступна по адресу `/docs/`).

## 🛠️ Стек технологий

| Категория          | Технологии |
| ------------------ | ---------- |
| **Backend**        | ![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white) ![Django REST Framework](https://img.shields.io/badge/DRF-ff1709?style=flat&logo=django&logoColor=white) |
| **База данных**    | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white) (также поддерживается SQLite) |
| **Аутентификация** | ![JWT](https://img.shields.io/badge/JWT-black?style=flat&logo=JSON%20web%20tokens) ![django-allauth](https://img.shields.io/badge/django--allauth-37a3b0?style=flat) |
| **Платежи**        | ![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=flat&logo=Stripe&logoColor=white) |
| **Документация**   | ![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=flat&logo=Swagger&logoColor=white) |
| **Другое**         | Celery, Redis, Gunicorn, WhiteNoise |

## 🚀 Быстрый старт (Установка и запуск)

Эти инструкции помогут вам запустить копию проекта на вашем локальном компьютере для разработки и тестирования.

### Предварительные требования

- Установленный **Python** (версия 3.10 или новее)
- Установленный **pip** (обычно идёт вместе с Python)
- **PostgreSQL** (опционально, для работы с базой данных)

### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/Omurbek000/Airbnb.git
cd Airbnb
