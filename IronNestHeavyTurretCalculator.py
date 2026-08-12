import os
import sys


def enable_ansi():
  if os.name == "nt":
    os.system("")


class Colors:
  HEADER = "\033[95m"
  CYAN = "\033[96m"
  GREEN = "\033[92m"
  YELLOW = "\033[93m"
  RED = "\033[91m"
  BOLD = "\033[1m"
  RESET = "\033[0m"


def get_direction_label(deg):
  deg = deg % 360
  if 337.5 <= deg <= 360 or 0 <= deg < 22.5:
    return "North"
  elif 22.5 <= deg < 67.5:
    return "Northeast"
  elif 67.5 <= deg < 112.5:
    return "East"
  elif 112.5 <= deg < 157.5:
    return "Southeast"
  elif 157.5 <= deg < 202.5:
    return "South"
  elif 202.5 <= deg < 247.5:
    return "Southwest"
  elif 247.5 <= deg < 292.5:
    return "West"
  elif 292.5 <= deg < 337.5:
    return "Northwest"
  return "Unknown"


def main():
  enable_ansi()
  print(f"{Colors.HEADER}==========================================")
  print(f"     {Colors.YELLOW}IRON NEST ARTILLERY CALCULATOR")
  print(f"      {Colors.CYAN}MADE WITH <3 @FLUFFYCYANNOVA")
  print(f" {Colors.RED}GLORY TO CASTILE! GLORY TO HIGH COMMAND!")
  print(f"{Colors.HEADER}=========================================={Colors.RESET}")
  print(f" Format: {Colors.BOLD}[Rotation] [Distance] [Powder]{Colors.RESET}")
  print(f" Example: {Colors.GREEN}137.7 4.29 1{Colors.RESET} (or omit powder for all possible elevation)")
  print(f" Type {Colors.YELLOW}'q'{Colors.RESET} or {Colors.YELLOW}'quit'{Colors.RESET} to exit.\n")

  while True:
    try:
      user_input = input(
          f"{Colors.BOLD}{Colors.CYAN}Target > {Colors.RESET}"
      ).strip()

      if user_input.lower() in ["q", "quit"]:
        print(
            f"\n{Colors.YELLOW}Exiting calculator. Good hunting!"
            f" {Colors.RESET}"
        )
        break

      if not user_input:
        continue

      parts = user_input.split()
      if len(parts) < 2:
        print(
            f"{Colors.RED}[!] Error: Please provide at least Rotation and"
            f" Distance.{Colors.RESET}\n"
        )
        continue

      rotation = float(parts[0])
      distance = float(parts[1])
      powder = int(parts[2]) if len(parts) > 2 else None

      direction = get_direction_label(rotation)
      base_calc = distance * 12
      max_elevation = 60.0

      print(f"\n{Colors.GREEN}Target locked!{Colors.RESET}")
      print(
          f"Rotation:  {Colors.BOLD}{rotation:06.2f}°{Colors.RESET}"
          f" ({direction})"
      )

      if powder is not None:
        elevation = base_calc / powder
        print(f"Distance:  {Colors.BOLD}{distance:.2f} km{Colors.RESET}")
        print(f"Elevation: {Colors.BOLD}{elevation:05.2f}°{Colors.RESET}")
        print(f"Powder:    {Colors.BOLD}{powder}x{Colors.RESET}")

        if elevation <= max_elevation:
          print(
              f"Status:    {Colors.GREEN}[✓] Safe (clears 60°"
              f" limit){Colors.RESET}\n"
          )
        else:
          print(
              f"Status:    {Colors.RED}[✗] WARNING: Exceeds 60°"
              f" limit!{Colors.RESET}\n"
          )
      else:
        print(f"Distance:  {Colors.BOLD}{distance:.2f} km{Colors.RESET}")
        print(f"Powder Options (1x - 6x):")
        for p in range(1, 7):
          elevation = base_calc / p
          if elevation <= max_elevation:
            status = f"{Colors.GREEN}[✓] Safe{Colors.RESET}"
          else:
            status = f"{Colors.RED}[✗] Exceeds Limit{Colors.RESET}"
          print(
              f"  • {p}x Powder -> Elevation:"
              f" {Colors.BOLD}{elevation:05.2f}°{Colors.RESET} [{status}]"
          )
        print()

    except ValueError:
      print(
          f"{Colors.RED}[!] Error: Invalid numbers entered. Please try"
          f" again.{Colors.RESET}\n"
      )
    except Exception as e:
      print(f"{Colors.RED}[!] An unexpected error occurred: {e}{Colors.RESET}\n")


if __name__ == "__main__":
  main()
  input(
      f"\n{Colors.YELLOW}Press Enter to close this window...{Colors.RESET}"
  )
