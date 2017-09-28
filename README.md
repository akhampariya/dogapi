# Django REST API Exercise Assignment

## Introduction

For this assignment I have created a basic Django Rest Api as instructed in [Building API endpoint exercise](https://mlhale.github.io/CYBR8470/modules/building-a-server/django-exercise.html)


## Specification for REST Api
The dogAPI endpoint, allows an end user to create a new `Dog` model by making a `POST` to `/dogapi/dogs`, view current dogs that have been saved to the server before by making a `GET` to `/dogapi/dogs`, and get, modify, or delete an existing `Dog` record by making a `GET`, `PUT`, or `DELETE` request (respectively) to `/api/dogs/<id>` where `<id>` is the id of the `Dog`  record to be retrieved, modified, or deleted.

The `Dog` includes a foreign key to the `Breed` endpoints for dog breed at `/dogapi/breeds/` and `/dogapi/breeds/<id>`. 

### Dog model

- name (a character string)
- age (an integer)
- breed (a foreign key to the Breed Model)
- gender (a character string)
- color (a character string) 
- favoritefood (a character string)
- favoritetoy (a character string)

### Breed Model

- name (a character string)
- size (a character string) [should accept Tiny, Small, Medium, Large]
- friendliness (an integer field) [should accept values from 1-5]
- trainability (an integer field) [should accept values from 1-5]
- sheddingamount (an integer field) [should accept values from 1-5]
- exerciseneeds (an integer field) [should accept values from 1-5]

### What I did 

 - added a `Dog` and `Breed` models to models.py
 - generated new migrations
 - migrated database to include tables for `Dog` and `Breed`
 - Used ModelViewSet
 - Tested the API    

### Note 
I was trying to put it on heroku so settings are modified but complete. Its working fine on dev.

## Ref

Ref - https://mlhale.github.io/CYBR8470/modules/building-a-server/django-exercise.html
