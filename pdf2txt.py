import pdfplumber as pb
 
file_handle=open('/file directory.txt',mode='w',encoding='utf-8')
# 读取PDF文档
pdf = pb.open("/file directory.pdf")
# 获取页数
a= len(pdf.pages)
print("当前页：",a)
print("-----------------------------------------")
 
i=0
for i in range(0, a):
    first_page = pdf.pages[i]
    print("本页：",first_page.page_number)
    print("-----------------------------------------")
    # 导出当前页文本
    text = first_page.extract_text()
    # print(text)
    file_handle.write(text)
