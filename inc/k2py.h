#ifndef __K2PY_DLL_H__
#define __K2PY_DLL_H__

#include <windows.h>

#define K2PY_DLL_EXPORTS

#ifdef __cplusplus
#define EXPORT_API extern "C" __declspec(dllexport)
#else
#define EXPORT_API __declspec(dllexport)
#endif

typedef struct _K2RESULT
{
	int nResult;
	WCHAR wResult[2048];
} K2RESULT, *PK2RESULT;

typedef BOOLEAN (*K2LOAD)(PWCHAR pwEnginePath, ULONG InstanceCount);
typedef VOID (*K2UNLOAD)();
typedef BOOLEAN (*K2VERSION)(PWCHAR pwVersion, ULONG cchVersion);
typedef int (*K2SCAN)(ULONG Instance, PWCHAR pwPath, PK2RESULT pK2Result, BOOLEAN bCure);

EXPORT_API BOOLEAN K2Load(PWCHAR pwEnginePath, ULONG InstanceCount);
EXPORT_API VOID K2Unload();
EXPORT_API BOOLEAN K2Version(PWCHAR pwVersion, ULONG cchVersion);
EXPORT_API int K2Scan(ULONG Instance, PWCHAR pwPath, PK2RESULT pK2Result, BOOLEAN bCure);

#endif // __K2PY_DLL_H__