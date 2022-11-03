from flask import Blueprint, flash, redirect, render_template, url_for

# from webapp.feedback.models import Feedback
from webapp.feedback.forms import ContactForm

blueprint = Blueprint("feedback", __name__, url_prefix="/feedback")


@blueprint.route("/")
def feedback():
    title = "Обратная связь"
    contact_form = ContactForm()
    return render_template("feedback/feedback.html", page_title=title, form=contact_form)


@blueprint.route("/process", methods=["GET", "POST"])
def feedback_process():
    form = ContactForm()
    if form.validate_on_submit():
        user_name = form.name.data
        user_email = form.email.data
        user_subject = form.subject.data
        user_message = form.message.data
        flash("Ваше обращение отправлено")
        return redirect(url_for("feedback.feedback"))
    return redirect(url_for("feedback.feedback"))
