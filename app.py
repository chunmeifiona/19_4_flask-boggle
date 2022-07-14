from flask import Flask, request, render_template, redirect, flash
from boggle import Boggle

boggle_game = Boggle()
