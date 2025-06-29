import os

def read_file(filename: str):
    with open(filename,'r') as f:
        return f.read()
            

def copy_files(path: str):
    with open(path, 'w')as f:
        content = read_file('sample,txt')
        if content is None:
            return False
        f.write(content)
        return True

def append_file(path):
    with open(path,'a')as f:
        f.write(read_file('sample,txt'))
        return True

def read_binary( path: str):
   with open(path,'rb')as f:
     return f.read()
   
def write_binary(path : str, data:bytes = read_binary('thendral.jpeg.jpg')):

  with open(path, 'wb')as f:
    f.write(data)
    return True

def main():
    if write_binary('image.jpeg'):
        print('File written successfully')
    else:
        print('File write failed')
if __name__ == "__main__":
    main()
