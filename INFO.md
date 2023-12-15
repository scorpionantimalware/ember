# Feature JSON format Description

| ``Feature`` | sha256 | md5 | appeared | label | avclass | histogram | byteentropy | strings | general | header | section | imports | exports | datadirectories |
|--------|--------|-----|----------|-------|---------|-----------|-------------|---------|---------|--------|---------|---------|---------|----------------|
| ``Datatype`` | string | string | string | int | string | list of integers | list of integers  | object | object | object | object | object | list | list of objects |

| ``strings`` | numstrings | avlength | printabledist | printables | entropy | paths | urls | registry | MZ |
|-------------|------------|----------|---------------|------------|---------|-------|------|----------|----|
| ``Datatype`` | int | double | list of integers | int | double | int | int | int | int |

| ``general`` | size | vsize | has_debug | exports | imports | has_relocations | has_resources | has_signature | has_tls | symbols |
|-------------|------|-------|-----------|---------|---------|-----------------|---------------|---------------|---------|---------|
| ``Datatype`` | int | int | int | int | int | int | int | int | int | int |

| ``header`` | coff | optional |
|------------|------|----------|
| ``Datatype`` | object | object |

| ``coff`` | timestamp | machine | characteristics |
|----------|-----------|---------|-----------------|
| ``Datatype`` | int | string | list of strings |

| ``optional`` | subsystem | dll_characteristics | magic | major_image_version | minor_image_version | major_linker_version | minor_linker_version | major_operating_system_version | minor_operating_system_version | major_subsystem_version | minor_subsystem_version | sizeof_code | sizeof_headers | sizeof_heap_commit |
|--------------|-----------|---------------------|-------|---------------------|---------------------|----------------------|----------------------|--------------------------------|--------------------------------|-------------------------|-------------------------|-------------|----------------|--------------------|
| ``Datatype`` | string | list of strings | string | int | int | int | int | int | int | int | int | int | int | int |

| ``section`` | entry | sections |
|-------------|-------|----------|
| ``Datatype`` | string | list of objects |

| ``sections`` | name | size | entropy | vsize | props |
|--------------|------|------|---------|-------|-------|
| ``Datatype`` | string | int | double | int | list |

| ``datadirectories`` | name | size | virtual_address |
|---------------------|------|------|-----------------|
| ``Datatype`` | string | int | int |
