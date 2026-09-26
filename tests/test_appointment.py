import sys
from pathlib import Path
# 自动把src文件夹加入搜索路径
sys.path.append(str(Path(__file__).parent.parent / "src"))

from main import VetAppointmentSystem

def test_create_appointment():
    system = VetAppointmentSystem()
    app = system.create_appointment(
        pet_name="TestPet",
        owner_name="TestOwner",
        contact="test@mail.com",
        appointment_time="2026-10-02 14:00",
        service_type="Vaccination"
    )
    assert app.pet_name == "TestPet"
    assert len(system.appointment_list) == 1
    print("✅ test_create_appointment passed")

if __name__ == "__main__":
    test_create_appointment()
