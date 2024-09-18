if __name__ == '__main__':
    PATH_TO_COMPRESSOR = 'I:\SteamLibrary\steamapps\common\GTFO\AssetBundleCompressor\AssetBundleCompressor.exe'
    ASSET_FOLDER = 'I:\SteamLibrary\steamapps\common\GTFO\BepInEx\Assets\AssetBundles'
    GTFO_DATA_FOLDER = 'I:\SteamLibrary\steamapps\common\GTFO\GTFO_Data'

    import os 
    import argparse
    import shutil
    import datetime
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, required=True, help='path to uncompressed bundle')

    args = parser.parse_args()

    if not os.path.exists(args.path):
        raise ValueError(f'{args.path} not found')
    if os.path.isdir(args.path):
        src_dir = args.path
        flist = list(os.listdir(args.path))
    else:
        src_dir, f = os.path.split(args.path) 
        flist = [f]

    src_dir_name = os.path.split(src_dir)[1]
    import subprocess
    for i, f in enumerate(flist):
        if f == src_dir_name or f.endswith('.manifest') or f.endswith('-compressed'): continue
        print(f'{i + 1}: {f}')
        path = os.path.join(src_dir, f) 

        subprocess.call([PATH_TO_COMPRESSOR, 
                         path, 
                         GTFO_DATA_FOLDER])
        path = path + '-compressed'
        shutil.copy2(path, ASSET_FOLDER)
    print(datetime.datetime.now())