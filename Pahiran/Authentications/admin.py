from django.contrib import admin
from Authentications.models import (
    CompanyDetails,
    CompanyPaymentDetails,
    PaymentDetails,
    TeamMember,
    ServicePrice,
    Profile
)

@admin.register(CompanyDetails)
class CompanyDetailsAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone', 'is_active', 'created_at')
    search_fields = ('company_name', 'email', 'phone')
    list_filter = ('is_active', 'created_at')

@admin.register(CompanyPaymentDetails)
class CompanyPaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('company', 'payment_method', 'is_active', 'created_at')
    list_filter = ('payment_method', 'is_active', 'created_at')
    search_fields = ('company__company_name',)

@admin.register(PaymentDetails)
class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user', 'payment_method', 'amount', 'status', 'created_at')
    list_filter = ('payment_method', 'status', 'created_at')
    search_fields = ('transaction_id', 'user__username')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'company', 'is_active', 'created_at')
    list_filter = ('role', 'is_active', 'created_at')
    search_fields = ('name', 'role', 'company__company_name')

@admin.register(ServicePrice)
class ServicePriceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'price', 'frequency', 'company', 'is_active', 'created_at')
    list_filter = ('frequency', 'is_active', 'created_at')
    search_fields = ('service_name', 'company__company_name')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'ph_num', 'gender', 'city', 'created_at')
    search_fields = ('user__username', 'full_name', 'ph_num', 'city')
    list_filter = ('gender', 'created_at')
