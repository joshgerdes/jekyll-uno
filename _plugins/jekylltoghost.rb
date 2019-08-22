# Jekyll-to-Ghost
#
# This Jekyll plugin exports your Markdown posts into a format that can be easily imported by Ghost.
# http://ghost.org
#
# Author: Matt Harzewski
# Copyright: Copyright 2013 Matt Harzewski
# License: GPLv2 or later
# Version: 1.0.0


require 'json'



module Jekyll



	class GhostPage < StaticFile

		def initialize(site, base, dir, name, contents)
			@site = site
			@base = base
			@dir  = dir
			@name = name
			@contents = contents
		end

		def write(dest)
			File.open(File.join(@site.config['destination'], 'ghost_export.json'), 'w') do |f|
				f.write(@contents.to_json.to_s)
			end
			true
		end

	end



	class JsonFileGenerator < Generator


		safe true


		def initialize(site)
			super
			@tags = []
			@postTagMap = Hash.new
		end


		def generate(site)

			converter = site.getConverterImpl(Jekyll::Converters::Markdown)
			ex_posts = []
			id = 0

			site.posts.each do |post|

				timestamp = post.date.to_i * 1000

				ex_post = {
					"id" => id,
					"title" => post.title,
					"slug" => post.slug,
					"markdown" => post.content,
					"html" => converter.convert(post.content),
					"image" => nil,
					"featured" => 0,
					"page" => 0,
					"status" => "published",
					"language" => "en_US",
					"meta_title" => nil,
        			"meta_description" => nil,
        			"author_id" => 1,
        			"created_at" => timestamp,
        			"created_by" => 1,
        			"updated_at" => timestamp,
        			"updated_by" => 1,
        			"published_at" => timestamp,
        			"published_by" => 1
				}

				ex_posts.push(ex_post)

				self.process_tags(id, post.tags, post.categories)
				id += 1
			end

			export_object = {
				"meta" => {
					"exported_on" => Time.now.to_i * 1000,
					"version" => "000"
				},
				"data" => {
					"posts" => ex_posts,
					"tags" => self.tag_objects,
					"posts_tags" => self.posts_tag_objects
				}
			}

			site.static_files << GhostPage.new(site, site.source, site.config['destination'], 'ghost_export.json', export_object)

		end


		def process_tags(postId, tags, categories)
			unique_tags = tags | categories
			unique_tags = unique_tags.map do |t|
				t = t.chomp(",")
				t = t.downcase
			end
			@tags = unique_tags | @tags

			@postTagMap[postId] = unique_tags
		end


		def tag_objects
			tag_array = []
			@tags.each do |tag|
				tag_array.push({
					"id" => tag_array.size,
					"name" => tag,
					"slug" => tag.downcase,
					"description" => ""
				})
			end
			return tag_array
		end

		def posts_tag_objects
			posts_tag_array = []
			@postTagMap.each do |post, tags|
				tags.each do |tag|
					posts_tag_array.push({
										"id" => (posts_tag_array.size + 1),
										"post_id" => post,
										"tag_id" => @tags.index(tag)
										})
				end
			end
			return posts_tag_array
		end

	end



end
