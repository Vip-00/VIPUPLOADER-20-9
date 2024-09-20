import logging   #scammer
import subprocess   #scammer
import datetime   #scammer
import asyncio   #scammer
import os   #scammer
import requests   #scammer
import time   #scammer
from p_bar import progress_bar   #scammer
import aiohttp   #scammer
import aiofiles   #scammer
import tgcrypto   #scammer
import concurrent.futures   #scammer
import subprocess   #scammer
from pyrogram.types import Message   #scammer
from pyrogram import Client, filters   #scammer
   #scammer
def duration(filename):   #scammer
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",   #scammer
                             "format=duration", "-of",   #scammer
                             "default=noprint_wrappers=1:nokey=1", filename],   #scammer
        stdout=subprocess.PIPE,   #scammer
        stderr=subprocess.STDOUT)   #scammer
    return float(result.stdout)   #scammer
       #scammer
def exec(cmd):   #scammer
        process = subprocess.run(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)   #scammer
        output = process.stdout.decode()   #scammer
        print(output)   #scammer
        return output   #scammer
        #err = process.stdout.decode()   #scammer
def pull_run(work, cmds):   #scammer
    with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:   #scammer
        print("Waiting for tasks to complete")   #scammer
        fut = executor.map(exec,cmds)   #scammer
async def aio(url,name):   #scammer
    k = f'{name}.pdf'   #scammer
    async with aiohttp.ClientSession() as session:   #scammer
        async with session.get(url) as resp:   #scammer
            if resp.status == 200:   #scammer
                f = await aiofiles.open(k, mode='wb')   #scammer
                await f.write(await resp.read())   #scammer
                await f.close()   #scammer
    return k   #scammer
   #scammer
   #scammer
async def download(url,name):   #scammer
    ka = f'{name}.pdf'   #scammer
    async with aiohttp.ClientSession() as session:   #scammer
        async with session.get(url) as resp:   #scammer
            if resp.status == 200:   #scammer
                f = await aiofiles.open(ka, mode='wb')   #scammer
                await f.write(await resp.read())   #scammer
                await f.close()   #scammer
    return ka   #scammer
   #scammer
   #scammer
   #scammer
def parse_vid_info(info):   #scammer
    info = info.strip()   #scammer
    info = info.split("\n")   #scammer
    new_info = []   #scammer
    temp = []   #scammer
    for i in info:   #scammer
        i = str(i)   #scammer
        if "[" not in i and '---' not in i:   #scammer
            while "  " in i:   #scammer
                i = i.replace("  ", " ")   #scammer
            i.strip()   #scammer
            i = i.split("|")[0].split(" ",2)   #scammer
            try:   #scammer
                if "RESOLUTION" not in i[2] and i[2] not in temp and "audio" not in i[2]:   #scammer
                    temp.append(i[2])   #scammer
                    new_info.append((i[0], i[2]))   #scammer
            except:   #scammer
                pass   #scammer
    return new_info   #scammer
   #scammer
   #scammer
def vid_info(info):   #scammer
    info = info.strip()   #scammer
    info = info.split("\n")   #scammer
    new_info = dict()   #scammer
    temp = []   #scammer
    for i in info:   #scammer
        i = str(i)   #scammer
        if "[" not in i and '---' not in i:   #scammer
            while "  " in i:   #scammer
                i = i.replace("  ", " ")   #scammer
            i.strip()   #scammer
            i = i.split("|")[0].split(" ",3)   #scammer
            try:   #scammer
                if "RESOLUTION" not in i[2] and i[2] not in temp and "audio" not in i[2]:   #scammer
                    temp.append(i[2])   #scammer
                       #scammer
                    # temp.update(f'{i[2]}')   #scammer
                    # new_info.append((i[2], i[0]))   #scammer
                    #  mp4,mkv etc ==== f"({i[1]})"    #scammer
                       #scammer
                    new_info.update({f'{i[2]}':f'{i[0]}'})   #scammer
   #scammer
            except:   #scammer
                pass   #scammer
    return new_info   #scammer
   #scammer
   #scammer
   #scammer
async def run(cmd):   #scammer
    proc = await asyncio.create_subprocess_shell(   #scammer
        cmd,   #scammer
        stdout=asyncio.subprocess.PIPE,   #scammer
        stderr=asyncio.subprocess.PIPE)   #scammer
   #scammer
    stdout, stderr = await proc.communicate()   #scammer
   #scammer
    print(f'[{cmd!r} exited with {proc.returncode}]')   #scammer
    if proc.returncode == 1:   #scammer
        return False   #scammer
    if stdout:   #scammer
        return f'[stdout]\n{stdout.decode()}'   #scammer
    if stderr:   #scammer
        return f'[stderr]\n{stderr.decode()}'   #scammer
   #scammer
       #scammer
       #scammer
       #scammer
def old_download(url, file_name, chunk_size = 1024 * 10):   #scammer
    if os.path.exists(file_name):   #scammer
        os.remove(file_name)   #scammer
    r = requests.get(url, allow_redirects=True, stream=True)   #scammer
    with open(file_name, 'wb') as fd:   #scammer
        for chunk in r.iter_content(chunk_size=chunk_size):   #scammer
            if chunk:   #scammer
                fd.write(chunk)   #scammer
    return file_name   #scammer
   #scammer
   #scammer
def human_readable_size(size, decimal_places=2):   #scammer
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:   #scammer
        if size < 1024.0 or unit == 'PB':   #scammer
            break   #scammer
        size /= 1024.0   #scammer
    return f"{size:.{decimal_places}f} {unit}"   #scammer
   #scammer
   #scammer
def time_name():   #scammer
    date = datetime.date.today()   #scammer
    now = datetime.datetime.now()   #scammer
    current_time = now.strftime("%H%M%S")   #scammer
    return f"{date} {current_time}.mp4"   #scammer
   #scammer
async def download_video(url,cmd, name):   #scammer
    download_cmd = f'{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args "aria2c: -x 16 -j 32"'   #scammer
    global failed_counter   #scammer
    print(download_cmd)   #scammer
    logging.info(download_cmd)   #scammer
    k = subprocess.run(download_cmd, shell=True)   #scammer
    if "visionias" in cmd and k.returncode != 0 and failed_counter <= 10:   #scammer
        failed_counter += 1   #scammer
        await asyncio.sleep(5)   #scammer
        await download_video(url, cmd, name)   #scammer
    failed_counter = 0   #scammer
    try:   #scammer
        if os.path.isfile(name):   #scammer
            return name   #scammer
        elif os.path.isfile(f"{name}.webm"):   #scammer
            return f"{name}.webm"   #scammer
        name = name.split(".")[0]   #scammer
        if os.path.isfile(f"{name}.mkv"):   #scammer
            return f"{name}.mkv"   #scammer
        elif os.path.isfile(f"{name}.mp4"):   #scammer
            return f"{name}.mp4"   #scammer
        elif os.path.isfile(f"{name}.mp4.webm"):   #scammer
            return f"{name}.mp4.webm"   #scammer
   #scammer
        return name   #scammer
    except FileNotFoundError as exc:   #scammer
        return os.path.isfile.splitext[0] + "." + "mp4"   #scammer
   #scammer
async def send_doc(bot: Client, m: Message,cc,ka,cc1,prog,count,name):   #scammer
    reply = await m.reply_text(f"**⚡⚡⚡ᴜᴘʟᴏᴀᴅɪɴɢ ...**\n**📚❰Name❱**-`{name}` \n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**")   #scammer
    time.sleep(1)   #scammer
    start_time = time.time()   #scammer
    await m.reply_document(ka,caption=cc1)   #scammer
    count+=1   #scammer
    await reply.delete (True)   #scammer
    time.sleep(1)   #scammer
    os.remove(ka)   #scammer
    time.sleep(3)    #scammer
   #scammer
async def send_vid(bot: Client, m: Message,cc,filename,thumb,name,prog):   #scammer
    await prog.delete (True)   #scammer
    reply = await m.reply_text(f"**⚡⚡⚡ᴜᴘʟᴏᴀᴅɪɴɢ ...**\n\n**📚❰Name❱**-`{name}` \n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n-═════━‧₊˚❀༉‧₊˚.━═════-")   #scammer
    subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)   #scammer
    
    try:   
        if thumb == "no":   #scammer
            thumbnail = f"{filename}.jpg"   #scammer
        else:   #scammer
            thumbnail = thumb   #scammer
    except Exception as e:   #scammer
        await m.reply_text(str(e))  #scammer
   #scammer
    dur = int(duration(filename))   #scammer
   #scammer
    start_time = time.time()   #scammer
   #scammer
    try:   #scammer
        await m.reply_video(filename,caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur, progress=progress_bar,progress_args=(reply,start_time))   #scammer
    except Exception:   #scammer
        await m.reply_document(filename,caption=cc, progress=progress_bar,progress_args=(reply,start_time))   #scammer
    os.remove(filename)   #scammer
   #scammer
    os.remove(f"{filename}.jpg")   #scammer
    await reply.delete (True)   #scammer
  
