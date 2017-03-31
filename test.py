#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
# https://github.com/LevPasha/Instagram-API-python

from InstagramAPI import InstagramAPI
import getpass

v_login = raw_input("Login: ")
v_password = getpass.getpass("Password: ")

#InstagramAPI = InstagramAPI("login", "password")
InstagramAPI = InstagramAPI(v_login, v_password)
InstagramAPI.login() # login
#InstagramAPI.tagFeed("cat") # get media list by tag #cat
#media_id = InstagramAPI.LastJson # last response JSON
#print media_id
#InstagramAPI.like(media_id["ranked_items"][0]["pk"]) # like first media
#InstagramAPI.getUserFollowers(media_id["ranked_items"][0]["user"]["pk"]) # get first media owner followers


def people_not_follow_me(InstagramAPI):
	InstagramAPI.getSelfUserFollowers()
	seguidores = InstagramAPI.LastJson

	InstagramAPI.getSelfUsersFollowing()
	seguidos = InstagramAPI.LastJson

	list_seguidores = []
	for i in seguidores["users"]:
		list_seguidores.append(i["pk"])

	list_seguidos = []
	for i in seguidos["users"]:
		list_seguidos.append(i["pk"])

	return (set(list_seguidos) - set(list_seguidores))

def people_I_not_follow(InstagramAPI):
	InstagramAPI.getSelfUserFollowers()
	seguidores = InstagramAPI.LastJson

	InstagramAPI.getSelfUsersFollowing()
	seguidos = InstagramAPI.LastJson

	list_seguidores = []
	for i in seguidores["users"]:
		list_seguidores.append(i["pk"])

	list_seguidos = []
	for i in seguidos["users"]:
		list_seguidos.append(i["pk"])

	return (set(list_seguidores) - set(list_seguidos))

def ufollow_people_not_follow_me(InstagramAPI):
	list_mid = people_not_follow_me(InstagramAPI)
	print list_mid
	for i in list_mid:
		InstagramAPI.unfollow(i)
		print "Follow: %s" % (InstagramAPI.LastJson["friendship_status"]["following"])

def follow_people_follow_me(InstagramAPI):
	list_mid = people_I_not_follow(InstagramAPI)
	print list_mid
	for i in list_mid:
		InstagramAPI.follow(i)
		print "Follow: %s" % (InstagramAPI.LastJson["friendship_status"]["following"])

def follow_user_tag(tag):
	InstagramAPI.getUserTags(tag)
	for i in InstagramAPI.LastJson["users"]:
		InstagramAPI.follow(i["pk"])


InstagramAPI.searchUsers("Sevilla")
for i in InstagramAPI.LastJson["users"]:
	print i["username"]
#import pdb; pdb.set_trace()