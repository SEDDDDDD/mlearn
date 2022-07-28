import struct


# 압축을 해제하고 저장한 바이너리 파일을 CSV 파일 형태로 변경작업
def to_csv(name, maxData):
    # 학습/테스트 데이터 파일과 학습/테스트 레이블파 일을 열기
    img_f = open("./mnist/" + name + "-images-idx3-ubyte", "rb")
    lbl_f = open("./mnist/" + name + "-labels-idx1-ubyte", "rb")
    csv_f = open("./mnist/" + name + ".csv", "w", encoding="utf-8")
# --------------------------1. 헤더 정보 읽기
    # struct.unpack("포멧", "파일내용")
    magic, img_count = struct.unpack(">II", img_f.read(8)) # unpack 함수의 포맷에서
                                                         # "I" 는 부호없는 정수(4byte)를 의미
                                                         #"B" 는 부호없는 정수 (1byte)
                                                         # ">" : 빅엔디안 / "<" : 리틀엔디안
    magic, lbl_count = struct.unpack(">II", lbl_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    print(f"1개이미지 행 개수 : {rows}")
    print(f"1개이미지 열 개수 : {cols}")


    print(f"magic number : {magic}")
    print(f"전체 이미지 개수 : {img_count}")
    

    # unpack : 하나의 데이터를 풀어서 여러 데이터로 쪼개어 놓는것
    # 포멧 : 바이너리 데이터를 어떤 기준으로 잘라서 표시할 것인지

    pixels = rows * cols        # 1개 이미지의 픽셀 개수

    magic, lbl_count = struct.unpack(">II", lbl_f.read(8))


# ---------------------------2. 이미지 데이터를 읽어서 CSV 저장하기
# 학습 데이터 정답 6만개
    for idx in range(lbl_count):
        if idx > maxData:  # idx 값이 maxData 개수 이상일때 빠져나오기
            break
            
        label = struct.unpack("B", lbl_f.read(1))[0]
        # print(label)      # label val(정답 숫자)

        bdata = img_f.read(pixels)
        # print(bdata)      # binary data

        sdata = list(map(lambda n:str(n), bdata))
        # print(sdata)        # string data list(이미지 데이터, 1개 리스트당 784 픽셀)
        
        csv_f.write(str(label) + ",")
        csv_f.write(",".join(sdata)+ "\r\n")

        #잘 저장됐는지 이미지 파일로 저장해서 테스트
        if idx < 10:
            s = "P2 28 8 255\n"     # PGM 형식으로 파일 만들기 위해 넣는 헤더
            # print(s)
            s += "".join(sdata)
            # print(s)
            iname = "./mnist/{0}-{1}-{2}.pgm".format(name, idx, label)
            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)
            # print(f)
    csv_f.close()
    img_f.close()
    lbl_f.close()

# 결과 출력
to_csv("train", 100)
#
to_csv("t10k", 50)