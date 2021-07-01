from os import link
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import importlib,sys 
importlib.reload(sys)


wp = Client('https://www.jiantong.com.tw/news//xmlrpc.php', 'news', 'news1234')
 
 
# filename = "./images/pikachu1.jpg"
# #上传的图片文件路径
 
# # prepare metadata
# data = {
#         'name': 'picture.jpg',
#         'type': 'image/jpeg',  # mimetype
# }
 
# # read the binary file and let the XMLRPC library encode it into base64
# with open(filename, 'rb') as img:
#         data['bits'] = xmlrpc_client.Binary(img.read())
 
# response = wp.call(media.UploadFile(data))

# attachment_id = response['id']
 
post = WordPressPost()
post.title = "快訊／北桃通勤確診女「上班路線曝」！搭捷運紅線到中山站"
post.content = '<h4 style="padding-bottom: 20px;">桃園昨日公布一名確診者（案14760）每天上班以台鐵換搭捷運方式通勤，「但生活算是相當規律」。對此，衛生局長王文彥今（29日）稍早也公布個案上班路線，「從中壢火車站搭到台北車站，再搭乘紅線捷運至中山站..</h4><br><a style="font-size:25px;" href="https://www.ettoday.net/news/news/20210629/2018571.html" target="_blank" >繼續閱讀</a><br><img style="margin-top:40px;" src="https://cdn2.ettoday.net/images/5717/c5717443.jpg" with="600" heigh="400" alt="圖"><br><h6 style="text-align:end; margin-top:40px; font-size:16px;">此圖片、文章來源 : ettoday新聞雲</h6>'
post.post_status = 'publish'  #文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
post.terms_names = {
	# 'post_tag': ['疫情'], #文章所属标签，没有则自动创建
	'category': ['政治'] #文章所属分类，没有则自动创建0
 }
# post.thumbnail = attachment_id #缩略图的id
post.id = wp.call(posts.NewPost(post))

