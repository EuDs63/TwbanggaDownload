import requests
from tqdm import tqdm  # 用于显示下载进度条

content = [
    {
        "contentId": "08C29AC7-068A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "孤獨反輾轉",
        "contentInfo": "第一集",
        "sort": 1,
        "isPublish": True,
        "onClick": 31684,
        "InfoLog": {
            "createDate": "2024-10-14T08:32:00.500Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:22:49.496Z",
            "UpdateBy": None
        }
    },
    {
        "contentId": "86CDCC35-078A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "明仔載再會",
        "contentInfo": "第二集",
        "sort": 2,
        "isPublish": True,
        "onClick": 6071,
        "InfoLog": {
            "createDate": "2024-10-14T08:35:05.376Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:16:51.040Z",
            "UpdateBy": None
        }
    },
    {
        "contentId": "BB91FF82-078A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "隨揣著跤手",
        "contentInfo": "第三集",
        "sort": 3,
        "isPublish": True,
        "onClick": 3925,
        "InfoLog": {
            "createDate": "2024-10-14T08:37:14.893Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:21:59.213Z",
            "UpdateBy": None
        }
    },
    {
        "contentId": "4AE3D798-088A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "跳懸跳低的查某囡仔",
        "contentInfo": "第四集",
        "sort": 4,
        "isPublish": True,
        "onClick": 3700,
        "InfoLog": {
            "createDate": "2024-10-14T08:45:08.573Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:16:43.163Z",
            "UpdateBy": None
        }
    },
    {
        "contentId": "3E0750A0-088A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "袂飛的魚仔",
        "contentInfo": "第五集",
        "sort": 5,
        "isPublish": True,
        "onClick": 3228,
        "InfoLog": {
            "createDate": "2024-10-14T08:45:18.743Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:04:37.560Z",
            "UpdateBy": None
        }
    },
    {
        "contentId": "786D165B-0A8A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "金澤八景",
        "contentInfo": "第六集",
        "sort": 6,
        "isPublish": True,
        "onClick": 2270,
        "InfoLog": {
            "createDate": "2024-10-14T08:57:43.893Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:04:58.843Z",
            "UpdateBy": None
        }
    },
    {
        "contentId": "6BF65322-0B8A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "去恁兜",
        "contentInfo": "第七集",
        "sort": 7,
        "isPublish": True,
        "onClick": 2017,
        "InfoLog": {
            "createDate": "2024-10-14T09:03:10.696Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:08:57.266Z",
            "UpdateBy": None
        }
    },
    {
        "contentId": "12D3B1CA-0B8A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "孤獨搖滾",
        "contentInfo": "第八集",
        "sort": 8,
        "isPublish": True,
        "onClick": 2968,
        "InfoLog": {
            "createDate": "2024-10-14T09:07:53.166Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:25:27.640Z",
            "UpdateBy": None
        }
    },
    {
        "contentId": "5F33D944-0C8A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "江之島的電扶梯",
        "contentInfo": "第九集",
        "sort": 9,
        "isPublish": True,
        "onClick": 1725,
        "InfoLog": {
            "createDate": "2024-10-14T09:11:18.110Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:22:16.073Z",
            "UpdateBy": None
        }
    },
    {
        "contentId": "B4BFCEA3-0C8A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "暗暝了後",
        "contentInfo": "第十集",
        "sort": 10,
        "isPublish": True,
        "onClick": 1477,
        "InfoLog": {
            "createDate": "2024-10-14T09:13:57.423Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:22:59.153Z",
            "UpdateBy": None
        }
    },
    {
        "contentId": "1ED6B708-0D8A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "十二進位法的黃昏",
        "contentInfo": "第十一集",
        "sort": 11,
        "isPublish": True,
        "onClick": 2291,
        "InfoLog": {
            "createDate": "2024-10-14T09:16:46.723Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:07:01.936Z",
            "UpdateBy": None
        }
    },
    {
        "contentId": "C3768571-0D8A-EF11-BC95-005056B2D58D",
        "contentType": "animation",
        "objType": None,
        "contentTitle": "早起的日頭光照佇你的身上",
        "contentInfo": "第十二集",
        "sort": 12,
        "isPublish": True,
        "onClick": 3998,
        "InfoLog": {
            "createDate": "2024-10-14T09:19:42.553Z",
            "createBy": None,
            "UpdateDate": "2024-11-20T14:01:23.636Z",
            "UpdateBy": None
        }
    }
]


def fetch_download_url(index):
    # 首先请求api,获取下载地址
    contentId = content[index - 1]["contentId"]

    INFO_API_URL_PREFIX = "https://twbangga.moe.edu.tw/server/web/animation/video/"

    info_api_url = f"{INFO_API_URL_PREFIX}{contentId}"

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    }

    try:
        response = requests.get(info_api_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(e)
        return None

# 下载视频
def download_video(video_url, video_name, save_path="."):
    try:
        # 设置请求头
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        }
        # 发起请求
        with requests.get(video_url, headers=headers, stream=True, timeout=10) as response:
            response.raise_for_status()  # 检查请求是否成功

            # 获取总大小
            total_size = int(response.headers.get("content-length", 0))
            chunk_size = 1024  # 每次读取的字节大小

            # 创建保存文件路径
            file_path = f"{save_path}/{video_name}.mp4"

            # 下载视频
            with open(file_path, "wb") as f, tqdm(
                    desc=video_name,
                    total=total_size,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
            ) as bar:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    f.write(chunk)
                    bar.update(len(chunk))

        print(f"视频已成功下载至: {file_path}")
        return file_path

    except requests.exceptions.RequestException as e:
        print(f"下载失败，发生网络错误: {e}")
    except Exception as e:
        print(f"下载失败，发生未知错误: {e}")
    return None

index = 4
download_info = fetch_download_url(index)
video_url = download_info["video"]["url"]
video_name = content[index - 1]["contentTitle"]
download_video(video_url, video_name)
