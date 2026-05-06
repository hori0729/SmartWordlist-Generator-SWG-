import os
import sys
import itertools
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(prompt, allow_skip=True):
    """Solicita input al usuario con opción de saltar."""
    if allow_skip:
        value = input(f"{prompt} (Enter para saltar): ").strip()
        return value if value else None
    return input(f"{prompt}: ").strip()

def date_variations(date_str):
    """Genera variaciones de una fecha."""
    variations = set()
    try:
        for fmt in ["%d/%m/%Y", "%d-%m-%Y", "%d/%m/%y", "%d-%m-%y",
                     "%m/%d/%Y", "%m-%d-%Y", "%Y/%m/%d", "%Y-%m-%d",
                     "%d%m%Y", "%d%m%y", "%m%d%Y", "%m%d%y", "%Y%m%d"]:
            try:
                dt = datetime.strptime(date_str, fmt)
                variations.add(dt.strftime("%d%m%Y"))
                variations.add(dt.strftime("%d%m%y"))
                variations.add(dt.strftime("%d-%m-%Y"))
                variations.add(dt.strftime("%d/%m/%Y"))
                variations.add(dt.strftime("%m%d%Y"))
                variations.add(dt.strftime("%m%d%y"))
                variations.add(dt.strftime("%Y%m%d"))
                variations.add(dt.strftime("%Y-%m-%d"))
                variations.add(str(dt.day))
                variations.add(str(dt.month))
                variations.add(str(dt.year))
                variations.add(str(dt.year)[2:])
                break
            except:
                continue
    except:
        variations.add(date_str)
    return variations

def process_name(name):
    """Procesa un nombre y genera variaciones (mayúsculas, minúsculas, reverso, etc)."""
    vars_set = set()
    name = name.strip()
    vars_set.add(name)
    vars_set.add(name.lower())
    vars_set.add(name.upper())
    vars_set.add(name.capitalize())
    vars_set.add(name[::-1])
    vars_set.add(name.lower()[::-1])
    vars_set.add(name.upper()[::-1])
    if len(name) > 2:
        vars_set.add(name[:3])
        vars_set.add(name[:3].upper())
    return vars_set

def leet_transform(text):
    """Variaciones con números y símbolos."""
    results = {text, text.lower(), text.upper(), text.capitalize()}
    suffixes = ['123', '1234', '12345', '1', '12', '!', '@', '#', '$',
                '2023', '2024', '2025', '2026', '0', '00', '000', '0000',
                '123!', '1234!', '2024!', '2025!']
    for suffix in suffixes:
        results.add(f"{text}{suffix}")
        results.add(f"{text.lower()}{suffix}")
        results.add(f"{text.upper()}{suffix}")
    return results

def add_numbers_symbols_years(words_set):
    """Añade números, símbolos y años a cada palabra."""
    expanded = set(words_set)
    numbers = ['1', '12', '123', '1234', '12345', '0', '00', '000', '0000']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '?', '.']
    years = ['2023', '2024', '2025', '2026', '23', '24', '25', '26']
    
    for w in words_set:
        w = str(w)
        for n in numbers:
            expanded.add(f"{w}{n}")
        for s in symbols:
            expanded.add(f"{w}{s}")
        for y in years:
            expanded.add(f"{w}{y}")
    return expanded

def main():
    clear_screen()
    print("=" * 70)
    print("   SmartWordlist Generator (SWG)")
    print("   Generador avanzado de wordlists basado en patrones humanos ")
    print("=" * 70)
    print("\n[!] USO AUTORIZADO - Prueba de penetración")
    print("[!] Ingresa los datos que tengas. Enter para saltar.\n")
    
    data = {}
    categorias_activas = []
    
    # ==========================================
    # 1. FECHA DE CUMPLEAÑOS
    # ==========================================
    print("\n┌─── FECHA DE CUMPLEAÑOS ───────────────┐")
    bday = get_input("  Fecha (DD/MM/AAAA)")
    if bday:
        data['birthday'] = date_variations(bday)
        print(f"  └→ {len(data['birthday'])} variaciones ✓")
        categorias_activas.append('birthday')
    else:
        data['birthday'] = set()
        print("  └→ Saltado")
    
    # ==========================================
    # 2. NOMBRE(S)
    # ==========================================
    print("\n┌─── NOMBRE(S) ─────────────────────────┐")
    names_raw = get_input("  Nombres (separados por espacio)")
    if names_raw:
        names = names_raw.split()
        name_vars = set()
        for name in names:
            name_vars.update(process_name(name))
        data['names'] = name_vars
        print(f"  └→ {len(data['names'])} variaciones ✓")
        categorias_activas.append('names')
    else:
        data['names'] = set()
        print("  └→ Saltado")
    
    # ==========================================
    # 3. APELLIDO(S)
    # ==========================================
    print("\n┌─── APELLIDO(S) ───────────────────────┐")
    lastnames_raw = get_input("  Apellidos (separados por espacio)")
    if lastnames_raw:
        lastnames = lastnames_raw.split()
        ln_vars = set()
        for ln in lastnames:
            ln_vars.update(process_name(ln))
        data['lastnames'] = ln_vars
        print(f"  └→ {len(data['lastnames'])} variaciones ✓")
        categorias_activas.append('lastnames')
    else:
        data['lastnames'] = set()
        print("  └→ Saltado")
    
    # ==========================================
    # 4. MASCOTA
    # ==========================================
    print("\n┌─── MASCOTA ───────────────────────────┐")
    pet = get_input("  Nombre de mascota")
    if pet:
        data['pet'] = process_name(pet)
        data['pet'].update(leet_transform(pet))
        print(f"  └→ {len(data['pet'])} variaciones ✓")
        categorias_activas.append('pet')
    else:
        data['pet'] = set()
        print("  └→ Saltado")
    
    # ==========================================
    # 5. EQUIPO FAVORITO
    # ==========================================
    print("\n┌─── EQUIPO FAVORITO ───────────────────┐")
    team = get_input("  Equipo favorito")
    if team:
        data['team'] = process_name(team)
        data['team'].update(leet_transform(team))
        print(f"  └→ {len(data['team'])} variaciones ✓")
        categorias_activas.append('team')
    else:
        data['team'] = set()
        print("  └→ Saltado")
    
    # ==========================================
    # 6. FAMILIARES
    # ==========================================
    print("\n┌─── FAMILIARES ────────────────────────┐")
    fam_raw = get_input("  Nombres (separados por coma)")
    if fam_raw:
        fam_names = [f.strip() for f in fam_raw.split(',') if f.strip()]
        fam_vars = set()
        for fname in fam_names:
            fam_vars.update(process_name(fname))
        data['family'] = fam_vars
        print(f"  └→ {len(data['family'])} variaciones ✓")
        categorias_activas.append('family')
    else:
        data['family'] = set()
        print("  └→ Saltado")
    
    # ==========================================
    # 7. AÑO ESPECIAL
    # ==========================================
    print("\n┌─── AÑO ESPECIAL ──────────────────────┐")
    special_year = get_input("  Año (graduación, boda, etc.)")
    if special_year:
        data['special_year'] = {special_year, special_year[2:] if len(special_year) == 4 else special_year}
        print("  └→ 1 año registrado ✓")
        categorias_activas.append('special_year')
    else:
        data['special_year'] = set()
        print("  └→ Saltado")
    
    # ==========================================
    # 8. OTROS DATOS
    # ==========================================
    print("\n┌─── OTROS DATOS ───────────────────────┐")
    other_raw = get_input("  Datos relevantes (separados por coma)")
    if other_raw:
        other_items = [o.strip() for o in other_raw.split(',') if o.strip()]
        other_vars = set()
        for item in other_items:
            other_vars.update(process_name(item))
            other_vars.update(leet_transform(item))
        data['other'] = other_vars
        print(f"  └→ {len(data['other'])} variaciones ✓")
        categorias_activas.append('other')
    else:
        data['other'] = set()
        print("  └→ Saltado")
    
    # ==========================================
    # VERIFICAR QUE HAYA ALGO
    # ==========================================
    if not categorias_activas:
        print("\n[!] No ingresaste ningún dato. No hay nada que generar.")
        sys.exit(1)
    
    # ==========================================
    # GENERAR TODO EN UNO
    # ==========================================
    print("\n" + "=" * 70)
    print(f"   CATEGORÍAS ACTIVAS: {len(categorias_activas)}")
    print("   GENERANDO WORDLIST COMPLETA...")
    print("=" * 70)
    
    etiquetas = {
        'birthday': 'Fecha nacimiento',
        'names': 'Nombres',
        'lastnames': 'Apellidos',
        'pet': 'Mascota',
        'team': 'Equipo',
        'family': 'Familiares',
        'special_year': 'Año especial',
        'other': 'Otros'
    }
    
    for cat in categorias_activas:
        print(f"  [✓] {etiquetas.get(cat, cat)}: {len(data[cat])} variaciones")
    
    # ──────────────────────────────────────────
    # PASO 1: Variaciones INDIVIDUALES de cada categoría
    # ──────────────────────────────────────────
    print("\n  [*] PASO 1/4: Variaciones individuales de cada categoría...")
    todo = set()
    
    for cat in categorias_activas:
        for w in data[cat]:
            todo.add(str(w))
        # Añadir números, símbolos y años
        todo.update(add_numbers_symbols_years(data[cat]))
    
    print(f"     → {len(todo):,} contraseñas individuales")
    
    # ──────────────────────────────────────────
    # PASO 2: Combinaciones de 2 palabras (MISMAS y DIFERENTES categorías)
    # ──────────────────────────────────────────
    print("  [*] PASO 2/4: Combinaciones de 2 palabras (todas las posibles)...")
    
    # Construir lista única de todas las palabras base
    all_words = set()
    for cat in categorias_activas:
        all_words.update(data[cat])
    all_words = sorted({str(w) for w in all_words if w and str(w).strip()})
    
    count_2 = 0
    for w1, w2 in itertools.permutations(all_words, 2):
        if count_2 >= 150000:  # límite de seguridad
            break
        for sep in ['', '.', '_', '-', '@', '#']:
            candidate = f"{w1}{sep}{w2}"
            todo.add(candidate)
            # Con año al final
            for yr in ['2024', '2025', '2026']:
                todo.add(f"{candidate}{yr}")
        count_2 += 1
    
    print(f"     → {len(todo):,} contraseñas (incluyendo combinaciones de 2)")
    
    # ──────────────────────────────────────────
    # PASO 3: Combinaciones de 3 palabras
    # ──────────────────────────────────────────
    print("  [*] PASO 3/4: Combinaciones de 3 palabras...")
    
    # Solo si no hay demasiadas palabras base
    if len(all_words) >= 3 and len(all_words) <= 30:
        count_3 = 0
        for w1, w2, w3 in itertools.permutations(all_words, 3):
            if count_3 >= 30000:
                break
            for sep in ['', '.', '_', '-']:
                todo.add(f"{w1}{sep}{w2}{sep}{w3}")
            count_3 += 1
    
    print(f"     → {len(todo):,} contraseñas (incluyendo combinaciones de 3)")
    
    # ──────────────────────────────────────────
    # PASO 4: Combinaciones cruzadas específicas por tipo
    # ──────────────────────────────────────────
    print("  [*] PASO 4/4: Combinaciones cruzadas específicas...")
    
    # nombre + fecha
    if 'names' in categorias_activas and 'birthday' in categorias_activas:
        for name in list(data['names'])[:25]:
            for fecha in list(data['birthday'])[:25]:
                todo.add(f"{name}{fecha}")
                todo.add(f"{name.lower()}{fecha}")
                todo.add(f"{fecha}{name}")
                todo.add(f"{name}.{fecha}")
                todo.add(f"{name}_{fecha}")
    
    # nombre + apellido
    if 'names' in categorias_activas and 'lastnames' in categorias_activas:
        for name in list(data['names'])[:20]:
            for ap in list(data['lastnames'])[:20]:
                todo.add(f"{name}{ap}")
                todo.add(f"{name}.{ap}")
                todo.add(f"{name}_{ap}")
                todo.add(f"{ap}{name}")
                for yr in ['2024', '2025']:
                    todo.add(f"{name}{ap}{yr}")
    
    # nombre + mascota
    if 'names' in categorias_activas and 'pet' in categorias_activas:
        for name in list(data['names'])[:20]:
            for pet in list(data['pet'])[:20]:
                todo.add(f"{name}{pet}")
                todo.add(f"{pet}{name}")
                todo.add(f"{name}.{pet}")
                todo.add(f"{name}_{pet}")
    
    # nombre + equipo
    if 'names' in categorias_activas and 'team' in categorias_activas:
        for name in list(data['names'])[:15]:
            for team in list(data['team'])[:15]:
                todo.add(f"{name}{team}")
                todo.add(f"{team}{name}")
                todo.add(f"{name}_{team}")
    
    # fecha + mascota
    if 'birthday' in categorias_activas and 'pet' in categorias_activas:
        for fecha in list(data['birthday'])[:20]:
            for pet in list(data['pet'])[:20]:
                todo.add(f"{fecha}{pet}")
                todo.add(f"{pet}{fecha}")
    
    # fecha + equipo
    if 'birthday' in categorias_activas and 'team' in categorias_activas:
        for fecha in list(data['birthday'])[:15]:
            for team in list(data['team'])[:15]:
                todo.add(f"{fecha}{team}")
                todo.add(f"{team}{fecha}")
    
    # nombre + familiar
    if 'names' in categorias_activas and 'family' in categorias_activas:
        for name in list(data['names'])[:15]:
            for fam in list(data['family'])[:15]:
                todo.add(f"{name}{fam}")
                todo.add(f"{fam}{name}")
    
    # nombre + fecha + mascota
    if 'names' in categorias_activas and 'birthday' in categorias_activas and 'pet' in categorias_activas:
        for name in list(data['names'])[:10]:
            for fecha in list(data['birthday'])[:10]:
                for pet in list(data['pet'])[:10]:
                    todo.add(f"{name}{fecha}{pet}")
                    todo.add(f"{name}{pet}{fecha}")
                    todo.add(f"{fecha}{name}{pet}")
    
    # nombre + fecha + equipo
    if 'names' in categorias_activas and 'birthday' in categorias_activas and 'team' in categorias_activas:
        for name in list(data['names'])[:10]:
            for fecha in list(data['birthday'])[:10]:
                for team in list(data['team'])[:10]:
                    todo.add(f"{name}{fecha}{team}")
                    todo.add(f"{team}{name}{fecha}")
    
    # nombre + apellido + fecha
    if 'names' in categorias_activas and 'lastnames' in categorias_activas and 'birthday' in categorias_activas:
        for name in list(data['names'])[:10]:
            for ap in list(data['lastnames'])[:10]:
                for fecha in list(data['birthday'])[:10]:
                    todo.add(f"{name}{ap}{fecha}")
                    todo.add(f"{name}.{ap}.{fecha}")
                    todo.add(f"{fecha}{name}{ap}")
    
    # mascota + año
    if 'pet' in categorias_activas and 'special_year' in categorias_activas:
        for pet in list(data['pet'])[:20]:
            for yr in data['special_year']:
                todo.add(f"{pet}{yr}")
                todo.add(f"{yr}{pet}")
    
    # equipo + año
    if 'team' in categorias_activas and 'special_year' in categorias_activas:
        for team in list(data['team'])[:20]:
            for yr in data['special_year']:
                todo.add(f"{team}{yr}")
                todo.add(f"{yr}{team}")
    
    # nombre + año
    if 'names' in categorias_activas and 'special_year' in categorias_activas:
        for name in list(data['names'])[:20]:
            for yr in data['special_year']:
                todo.add(f"{name}{yr}")
                todo.add(f"{yr}{name}")
    
    # fecha + año
    if 'birthday' in categorias_activas and 'special_year' in categorias_activas:
        for fecha in list(data['birthday'])[:20]:
            for yr in data['special_year']:
                todo.add(f"{fecha}{yr}")
                todo.add(f"{yr}{fecha}")
    
    # Combinaciones con familiares + otros datos
    if 'family' in categorias_activas and 'other' in categorias_activas:
        for fam in list(data['family'])[:15]:
            for other in list(data['other'])[:15]:
                todo.add(f"{fam}{other}")
                todo.add(f"{other}{fam}")
    
    # Otras combinaciones con 'otros datos'
    if 'other' in categorias_activas:
        for other in list(data['other'])[:15]:
            for cat in categorias_activas:
                if cat != 'other' and data[cat]:
                    for w in list(data[cat])[:10]:
                        todo.add(f"{other}{w}")
                        todo.add(f"{w}{other}")
    
    # ==========================================
    # FILTRAR Y ORDENAR
    # ==========================================
    print("\n  [*] Ordenando y filtrando...")
    final_wordlist = sorted([str(p) for p in todo if len(str(p)) >= 4])
    
    # ==========================================
    # NOMBRE DEL ARCHIVO
    # ==========================================
    print("\n" + "-" * 70)
    default_name = f"wordlist_completa_{len(final_wordlist)}_pass.txt"
    output_file = input(f"  Nombre del archivo (Enter para '{default_name}'): ").strip()
    if not output_file:
        output_file = default_name
    if not output_file.endswith('.txt'):
        output_file += '.txt'
    
    if os.path.exists(output_file):
        sobrescribir = input(f"\n  [!] '{output_file}' ya existe. ¿Sobrescribir? (s/N): ").strip().lower()
        if sobrescribir != 's':
            output_file = input("  Nuevo nombre: ").strip()
            if not output_file.endswith('.txt'):
                output_file += '.txt'
    
    # ==========================================
    # GUARDAR
    # ==========================================
    print(f"\n  [*] Guardando {len(final_wordlist):,} contraseñas en '{output_file}'...")
    
    with open(output_file, 'w', encoding='utf-8', errors='ignore') as f:
        for i, password in enumerate(final_wordlist):
            f.write(password + '\n')
            # Mostrar progreso cada 100,000
            if (i + 1) % 100000 == 0:
                print(f"     → {(i+1):,} escritas...")
    
    file_size_kb = os.path.getsize(output_file) / 1024
    file_size_mb = file_size_kb / 1024
    
    # ==========================================
    # RESUMEN FINAL
    # ==========================================
    print("\n" + "=" * 70)
    print("   ✅ WORDLIST GENERADA - TODO EN UNO")
    print("=" * 70)
    print(f"   Archivo: {output_file}")
    print(f"   Ruta:    {os.path.abspath(output_file)}")
    print(f"   Total:   {len(final_wordlist):,} contraseñas")
    if file_size_mb > 1:
        print(f"   Tamaño:  {file_size_mb:.2f} MB")
    else:
        print(f"   Tamaño:  {file_size_kb:.2f} KB")
    
    # Resumen de categorías usadas
    print(f"\n   Categorías incluidas:")
    for cat in categorias_activas:
        print(f"     • {etiquetas.get(cat, cat)}: {len(data[cat])} palabras base")
    
    # Mostrar muestras variadas
    print(f"\n   ─── MUESTRA (20 de {len(final_wordlist):,}) ───")
    # Mostrar algunas individuales
    print("   [Individuales]")
    for p in final_wordlist[:5]:
        print(f"     {p}")
    # Mostrar algunas combinadas
    print("   [Combinaciones]")
    mid = len(final_wordlist) // 2
    for p in final_wordlist[100:105]:
        print(f"     {p}")
    print("   ...")
    
    print(f"\n{'=' * 70}")
    print("   WORDLIST GENERADA - USO AUTORIZADO")
    print(f"{'=' * 70}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Generación interrumpida por el usuario.")
        sys.exit(0)
    except MemoryError:
        print("\n[!] ERROR: Memoria insuficiente.")
        print("[!] Ingresa menos datos o usa palabras más cortas.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] Error: {e}")
        sys.exit(1)
