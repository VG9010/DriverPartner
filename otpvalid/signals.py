from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils import timezone
from .models import OtpToken
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            return  # Skip OTP for superusers

        # Create OTP token
        otp_token = OtpToken.objects.create(
            user=instance,
            otp_expires_at=timezone.now() + timezone.timedelta(minutes=5),
        )

        # Deactivate the user until email verification
        instance.is_active = False
        instance.save()

        # Fetch the latest OTP token
        otp = OtpToken.objects.filter(user=instance).last()

        if not otp:
            # Log or handle the error if OTP creation failed
            print(f"Failed to create OTP for user: {instance.username}")
            return

        # Email credentials
        subject = "Email Verification"
        message = f"""
        Hi {instance.username}, here is your OTP {otp.otp_code}
        It expires in 5 minutes. Use the URL below to redirect back to the website:
        http://127.0.0.1:8000/verify-email/{instance.username}
        """

        sender = "no-reply@example.com"  # Update this with your sender email
        receiver = [instance.email]

        # Send email
        try:
            send_mail(
                subject,
                message,
                sender,
                receiver,
                fail_silently=False,
            )
            print(f"OTP email sent to {instance.email}.")
        except Exception as e:
            print(f"Failed to send OTP email to {instance.email}: {e}")



# signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
