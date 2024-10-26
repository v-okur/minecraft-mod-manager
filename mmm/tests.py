import argparse

def main():
    parser = argparse.ArgumentParser(description='Mod yükleme aracı')

    parser.add_argument('mods', nargs="*", help='Yüklemek istediğiniz modlar')
    parser.add_argument('-m', '--min', action='append', help='Her mod için opsiyonel minimum değer. Format: mod1:10 mod2:5')
    parser.add_argument('-M', '--max', action='append', help='Her mod için opsiyonel maksimum değer. Format: mod1:20 mod2:15')

    args = parser.parse_args()

    # Mod isimlerini ve opsiyonel değerleri ayır
    mod_options = {}
    
    # Varsayılan değerler
    for mod in args.mods:
        mod_options[mod] = {'min': None, 'max': None}
    
    # Minimum değerleri ata
    if args.min:
        for min_option in args.min:
            mod_name, min_value = min_option.split(':')
            mod_options[mod_name]['min'] = int(min_value)

    # Maksimum değerleri ata
    if args.max:
        for max_option in args.max:
            mod_name, max_value = max_option.split(':')
            mod_options[mod_name]['max'] = int(max_value)

    # Sonuçları yazdır
    for mod, options in mod_options.items():
        print(f"Mod: {mod}, Minimum: {options['min']}, Maksimum: {options['max']}")

if __name__ == '__main__':
    main()
