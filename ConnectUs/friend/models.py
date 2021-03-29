# from django.db import models
# from django.conf import settings
# from django.utils import timezone
# # Create your models here.
#
#
# class FriendList(models.Model):
#
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="friends")
#     friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True , related_name="friends" )
#
#
#     def __str__(self):
#         return self.user.username
#
#     def add_friends(self):
#
#
#         if not account in self.friends.all():
#             self.friends.add(account)
#
#     def remove_friends(self):
#
#
#         if not account in self.friends.all():
#             self.friends.remove(account)
#
#     def unfriend(self, removee):
#
#         remover_friends_list = self
#
#         remover_friends_list.remove_friends(removee)
#
#         friend_list = FriendList.object.get(username=removee)
#         friend_list.remove_friend(self.user)
#
#     def is_mutual_friend(self,friend):
#
#         if friend in self.friends.all():
#             return True
#         return False
#
#
#
# class FriendRequest(models.Model):
#     """
#     1.sender : person sending request
#     2.receiver : person receiving request
#     """
#     sender = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE ,related_name="sender")
#     receiver = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE ,related_name="receiver")
#     is_active = models.BooleanField(blank=True , null=False, default=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#
#     def __str__(self):
#         return self.sender.username
#
#     def accept(self):
#         """
#         accept friend list
#         """
#
#         receiver_friend_list = FriendList.object.get(user=self.receiver)
#
#         if receiver_friend_list:
#             receiver_friend_list.add_friend(self.sender)
#             sender_friend_list = FriendList.object.get(user=self.sender)
#             if sender_friend_list:
#                 sender_friend_list.add_friend(self.receiver)
#                 self.is_active = False
#                 self.save()
#
#
#     def decline(self):
#         """
#         Decline Friend request
#         """
#         self.is_active = False
#         self.save()
#
#     def cancle(self):
#         """
#         Cancle Friend request
#         """
#
#         self.is_active = False
#         self.save()
#
#
#
#
#
