from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin


from KYusers.models import KYProfile, CAProfile,College,Message,Key

class KYprofileInline(admin.StackedInline):
    model = KYProfile
    can_delete = False

class UserAdmin(UserAdmin):

    def name(obj):
        return "%s %s" % (obj.first_name, obj.last_name)

    def college(obj):
        return obj.kyprofile.college

    def mobileNumber(obj):
        return obj.kyprofile.mobileNumber

    def is_ca(obj):
        if obj.kyprofile.is_ca == True:
            if obj.kyprofile.caprofile.isChoosen:
                return True
        else:
            return False

    name.short_description = 'Name'
    college.short_description = 'College'
    mobileNumber.short_description = 'Mobile No.'
    list_filter = ()
    list_display = ('email',name, college, mobileNumber, is_ca)

class CollegeAdmin(admin.ModelAdmin):

    def Registrations(obj):
        number = KYProfile.objects.filter(college=obj).count()
        return number

    list_max_show_all = 500
    list_display = ('collegeName', 'collegeId',Registrations)
    ordering = ('collegeId','collegeName')
    search_fields = ('collegeName','collegeId')

class CAInline(admin.StackedInline):
    model = CAProfile

class KYProfileAdmin(admin.ModelAdmin):

    def name(obj):
        return obj.user.first_name

    def email(obj):
        return obj.user.email

    def caId(obj):
        try:
            id_ = obj.caprofile.caId
        except:
            id_ = 'NA'
        return id_

    def ca(obj):
        try:
            status = obj.caprofile.isChoosen
        except:
            status = 'NA'
        return status

    # def collegelist(obj):
    #     colleges =  College.objects.filter(regCount=True)
    #     return colleges

    list_max_show_all = 500
    list_filter = ('is_ca','college__regCount','college__collegeName')
    list_display = ('kyId',name,email,'college','mobileNumber',ca,caId)
    search_fields = ('kyId','college__collegeName', 'user__first_name')
    inlines = [
        CAInline,
    ]
class CAProfileAdmin(admin.ModelAdmin):

    def name(obj):
        return obj.kyprofile.user.first_name

    def email(obj):
        return obj.kyprofile.user.email

    def college(obj):
        return obj.kyprofile.college

    def mobileNumber(obj):
        return obj.kyprofile.mobileNumber

    def RegNum(obj):
        return obj.regNum

    list_filter = ('isChoosen',)
    list_display = ('caId',email,name,college,mobileNumber,RegNum)
    search_fields = ('caId','kyprofile__college__collegeName', 'kyprofile__user__first_name')

class MessageAdmin(admin.ModelAdmin):
    def name(obj):
        return obj.name
    def email(obj):
        return obj.email
    def number(obj):
        return obj.mobileNumber

    list_display = (name,email,number, 'mark_read')
    list_filter = ('mark_read',)
    search_fields = ('name','email', 'subject')


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User,UserAdmin)
admin.site.register(CAProfile,CAProfileAdmin)
admin.site.register(KYProfile,KYProfileAdmin)
admin.site.register(College,CollegeAdmin)
admin.site.register(Key)
admin.site.register(Message, MessageAdmin)
